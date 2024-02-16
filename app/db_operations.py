import json
import pandas as pd
from database import get_database_connection

conn = get_database_connection()

def insert_bank_branch(code, name):
    cursor = conn.cursor()
    query = "INSERT INTO banks_master(code, name) VALUES (%s, %s)"
    branch = (code, name)

    cursor.execute(query, branch)
    conn.commit()
    cursor.close()

def find_branch_by_code(branch_code):
    cursor = conn.cursor()
    query = "SELECT code, name FROM banks_master WHERE code = %s"
    cursor.execute(query, (branch_code,)) 

    rows = cursor.fetchall()
    cursor.close()
    return rows

def find_product_by_code(code):
    cursor = conn.cursor()
    query = "SELECT code, name FROM products_master WHERE code = %s"
    cursor.execute(query, (code,)) 

    rows = cursor.fetchall()
    cursor.close()
    return rows

def insert_product(code, name):
    cursor = conn.cursor()
    query = "INSERT INTO products_master(code, name) VALUES (%s, %s)"
    product = (code, name)

    cursor.execute(query, product)
    conn.commit()
    cursor.close()

def insert_prospect(account_number, name, mobile_number, address):
    cursor = conn.cursor()
    query = "INSERT INTO prospects_master(name, mobile_number, address, account_number) VALUES (%s, %s, %s, %s)"
    prospect = (name, mobile_number, address, account_number)

    cursor.execute(query, prospect)
    conn.commit()
    cursor.close()

def insert_branch_details(branches):
    for (code, name) in branches.values:
        bank_branch = find_branch_by_code(code)

        if not bool(bank_branch):
            insert_bank_branch(code, name)

def insert_product_details(products):
    for (code, name) in products.values:
        product = find_product_by_code(code)

        if not bool(product):
            insert_product(code, name)

def insert_prospect_details(prospects):
    for (account_number, name, mobile_number, address) in prospects.values:
        insert_prospect(account_number, name, mobile_number, address)

        
def insert_loan(loan_json):
    cursor = conn.cursor()
    loan = json.loads(loan_json)
    query = "INSERT INTO loans_master(account_number, disbursed_amount, disbursement_date, interest_rate, total_tenure, cif_id, branch_code, product_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    detail = (loan['Loan_Account_Number'], loan['Loan_Amount_Disbursed'], loan['Loan_Disbursement_Date'], loan['Roi'], loan['Total_Tenure'], loan['Cif_Id'], loan['Branch_Code'], loan['Product_Id'])

    cursor.execute(query, detail)
    conn.commit()
    cursor.close()
    
def insert_loan_details(loans):
    for row in loans.to_dict(orient='records'):
        for key, value in row.items():
            if isinstance(value, pd.Timestamp):
                row[key] = value.strftime('%Y-%m-%d')
        
        loan_json = json.dumps(row)
        insert_loan(loan_json)

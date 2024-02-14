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


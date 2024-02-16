import pandas as pd

def load_data():
    df = pd.read_excel('./data/demand_data.xlsx')
    return df

def process(df):
    validate_data = df.dropna()
    invalidate_data = df[df.isnull().any(axis=1)]

    unique_branches = validate_data.drop_duplicates(subset='Branch_Code')[['Branch_Code', 'Branch_Name']]
    unique_products = validate_data.drop_duplicates(subset='Product_Id')[['Product_Id','Product_Name']]
    prospects = validate_data[['Loan_Account_Number', 'Customer_Name', 'Mobile_Number', 'Customer_Address']]
    loans = validate_data[['Loan_Account_Number', 'Loan_Amount_Disbursed', 'Loan_Disbursement_Date', 
                'Roi', 'Total_Tenure', 'Cif_Id', 'Branch_Code', 'Product_Id']]
    emis = validate_data[['Loan_Account_Number', 'Emi_Due_Date', 'Loan_Outstanding', 'Principal_Outstanding', 
               'Interest_Outstanding', 'Emi_Amount', 'Principal_Amount', 'Interest_Amount', 
               'Arrear_Amount', 'Principal_Arrear', 'Interest_Arrear', 'Other_Charges', 'Last_Payment_Date',
               'Total_Amount_Collection', 'Dpd', 'Last_Paid_Amount', 'Last_Emi_Date', 'Current_Tenure',
               'Residual_Tenure', 'UnPaid_Installments', 'Total_Installments']]

    return unique_branches, unique_products, prospects, loans, emis


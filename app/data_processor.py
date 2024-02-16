import pandas as pd

def load_data():
    df = pd.read_excel('./data/sample.xlsx')
    return df

def process(df):
    validate_data = df.dropna()
    invalidate_data = df[df.isnull().any(axis=1)]

    unique_branches = validate_data.drop_duplicates(subset='Branch_Code')[['Branch_Code', 'Branch_Name']]
    unique_products = validate_data.drop_duplicates(subset='Product_Id')[['Product_Id','Product_Name']]
    prospects = df[['Loan_Account_Number', 'Customer_Name', 'Mobile_Number', 'Customer_Address']]
    loans = df[['Loan_Account_Number', 'Loan_Amount_Disbursed', 'Loan_Disbursement_Date', 
                'Roi', 'Total_Tenure', 'Cif_Id', 'Branch_Code', 'Product_Id']]

    return unique_branches, unique_products, prospects, loans


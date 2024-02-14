import pandas as pd

def load_data():
    df = pd.read_excel('./data/sample.xlsx')
    return df

def process(df):
    validate_data = df.dropna()
    invalidate_data = df[df.isnull().any(axis=1)]

    unique_branches = validate_data.drop_duplicates(subset='Branch_Code')[['Branch_Code', 'Branch_Name']]
    unique_products = validate_data.drop_duplicates(subset='Product_Id')[['Product_Id','Product_Name']]
    return unique_branches, unique_products


from flask import Flask
from database import get_database_connection
from create_tables import create_tables
from data_processor import load_data, process
from db_operations import insert_branch_details
from db_operations import insert_product_details
from db_operations import insert_prospect_details
from db_operations import insert_loan_details
from db_operations import insert_emi_details

# Connect to database
conn = get_database_connection()
if conn:
    print('Connected to the database.')

# Create tables
create_tables(conn)

# Loading data
df = load_data()
branches, products, prospects, loans, emis = process(df)
insert_branch_details(branches)
insert_product_details(products)
insert_prospect_details(prospects)
insert_loan_details(loans)
insert_emi_details(emis)

app = Flask(__name__)
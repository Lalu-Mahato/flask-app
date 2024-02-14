from flask import Flask
from database import get_database_connection
from create_tables import create_tables
from data_processor import load_data, process
from db_operations import insert_branch_details
from db_operations import insert_product_details

# Connect to database
conn = get_database_connection()

# Create tables
create_tables(conn)

# Loading data
df = load_data()
branches, products = process(df)
insert_branch_details(branches)
insert_product_details(products)

app = Flask(__name__)
import psycopg2

def get_database_connection():
    try:
        return psycopg2.connect(
            host="localhost",
            database="testdb",
            user="postgres",
            password="postgres"
        )
    except psycopg2.Error as e:
        print('Unable to connect to the database', e)

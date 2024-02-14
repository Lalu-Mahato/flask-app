import psycopg2

def get_database_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="testdb",
            user="postgres",
            password="postgres"
        )
        print('Connected to the database.')
        return conn
    except psycopg2.Error as e:
        print('Unable to connect to the database', e)

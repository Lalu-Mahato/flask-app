import psycopg2

def create_tables(conn):
    commands = (
        """
            CREATE TABLE IF NOT EXISTS banks_master (
                id SERIAL PRIMARY KEY,
                code INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS products_master (
                id SERIAL PRIMARY KEY,
                code INTEGER NOT NULL,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    try:
        with conn.cursor() as cur:
            for command in commands:
                cur.execute(command)
        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

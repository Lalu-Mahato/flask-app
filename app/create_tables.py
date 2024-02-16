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
        """,
        """
            CREATE TABLE IF NOT EXISTS prospects_master (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                mobile_number VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                account_number BIGINT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS loans_master (
                id SERIAL PRIMARY KEY,
                account_number BIGINT NOT NULL,
                disbursed_amount FLOAT NOT NULL,
                disbursement_date VARCHAR(255) NOT NULL,
                interest_rate FLOAT NOT NULL,
                total_tenure INTEGER NOT NULL,
                cif_id VARCHAR(255) NOT NULL,
                branch_code INTEGER NOT NULL,
                product_code INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS emis_master (
                id SERIAL PRIMARY KEY,
                account_number BIGINT NOT NULL,
                emi_due_date VARCHAR(255) NOT NULL,
                loan_outstanding FLOAT NOT NULL,
                principal_outstanding FLOAT NOT NULL,
                interest_outstanding FLOAT NOT NULL,
                emi_amount FLOAT NOT NULL,
                principal_amount FLOAT NOT NULL,
                interest_amount FLOAT NOT NULL,                
                arrear_Amount FLOAT NOT NULL,
                principal_arrear FLOAT NOT NULL,
                interest_arrear FLOAT NOT NULL,
                other_charges FLOAT NOT NULL,
                total_amount_collection FLOAT NOT NULL,
                dpd_days INTEGER NOT NULL,
                last_payment_date VARCHAR(255) NOT NULL,
                last_paid_amount FLOAT NOT NULL,
                last_emi_date VARCHAR(255) NOT NULL,
                current_tenure INTEGER NOT NULL,
                residual_tenure INTEGER NOT NULL,
                unpaid_installments INTEGER NOT NULL,
                total_installments INTEGER NOT NULL,
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

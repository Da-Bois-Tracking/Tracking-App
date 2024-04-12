import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def users_table():
    # Connection parameters
    connection_params = "dbname='tracking_app' user='postgres' host='postgres' port='5432' password='tracking_app_password'"

    # Connect to your database
    conn = psycopg2.connect(connection_params)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create a cursor object
    cur = conn.cursor()

    # SQL statement for creating the table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        member_since DATE NOT NULL DEFAULT current_date,
        date_of_birth DATE,
        phone_number VARCHAR(15),
        country VARCHAR(50),
        state VARCHAR(50),
        city VARCHAR(50),
        weight FLOAT,
        height_cm FLOAT,
        skill_level VARCHAR(15),
        position VARCHAR(10)
    );
    """

    # Execute the SQL statement
    cur.execute(create_table_sql)

    # Close the cursor and the connection
    cur.close()
    conn.close()

    print("Users table created successfully.")


# Run the function
users_table()

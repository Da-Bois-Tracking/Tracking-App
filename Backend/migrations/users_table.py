import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()


def users_table():
    # Connection parameters
    connection_params = {
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    }

    # Construct DSN (Data Source Name) string
    dsn = " ".join([f"{key}={value}" for key, value in connection_params.items()])

    # Connect to your database
    conn = psycopg2.connect(dsn)
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

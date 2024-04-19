import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_table():
    # Connection parameters - adjust these with your database details
    connection_params = "dbname='tracking_app' user='postgres' host='postgres' port='5432' password='tracking_app_password'"

    # Connect to your database
    conn = psycopg2.connect(connection_params)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create a cursor object
    cur = conn.cursor()

    # SQL statement for creating the table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT
    );
    """

    # Execute the SQL statement
    cur.execute(create_table_sql)

    # Close the cursor and the connection
    cur.close()
    conn.close()

    print("Table created successfully.")


# Run the function
create_table()

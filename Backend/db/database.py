import psycopg2

# Database connection parameters
db_params = {
    "dbname": "tracking_app_db",
    "user": "postgres",
    "password": "tracking_app_password",
    "host": "localhost",
    "port": "5432",
}


# Function to create tables
def create_tables():
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Create users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
        """
    )

    # Commit changes and close cursor/connection
    connection.commit()
    cursor.close()
    connection.close()


# Run the migration script
if __name__ == "__main__":
    create_tables()

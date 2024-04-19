import os
from psycopg2 import pool
import time

DATABASE_URL = os.environ.get("DATABASE_URL")


def create_connection_pool(max_retries=3, retry_delay=5):
    retries = 0
    while retries < max_retries:
        try:
            connection_pool = pool.SimpleConnectionPool(1, 10, DATABASE_URL)
            if connection_pool:
                print("Connection pool created successfully")
                return connection_pool
        except Exception as e:
            print(f"Error creating connection pool: {e}")
            retries += 1
            time.sleep(retry_delay)
    print("Max retries reached. Connection pool creation failed")
    return None


connection_pool = create_connection_pool()

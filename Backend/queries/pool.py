import os
from psycopg2 import pool

DATABASE_URL = os.environ.get("DATABASE_URL")

connection_pool = pool.SimpleConnectionPool(1, 10, dsn=DATABASE_URL)

if connection_pool:
    print("Connection pool created successfully")

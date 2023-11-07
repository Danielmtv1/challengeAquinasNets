from contextlib import contextmanager
import mysql.connector
import os

@contextmanager
def get_mysql_connection():
    connection = mysql.connector.connect(
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        host="mysql",
        database=os.environ.get("MYSQL_DATABASE")
    )
    try:
        yield connection
    finally:
        connection.close()

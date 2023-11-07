import subprocess
import time
import mysql.connector
import os


def wait_for_mysql():
    while True:
        try:
            connection = mysql.connector.connect(
                user=os.environ.get("MYSQL_USER"),
                password=os.environ.get("MYSQL_PASSWORD"),
                host="alquinas-mysql",
                database=os.environ.get("MYSQL_DATABASE")
            )
            connection.close()
            print("MySQL connect...")
            break
        except mysql.connector.Error:
            print("Waiting for MySQL...")
            time.sleep(1)


def run_alembic_autogenerate():
    wait_for_mysql()

    subprocess.run(["alembic", "-c", "alembic.ini", "upgrade", "head"])

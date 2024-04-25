import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    """create a database connection to a SQLite database"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="python-web-hw6",
            user="postgres",
            password="superpostgrespassword11",
        )
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError("Could not connect {err}")

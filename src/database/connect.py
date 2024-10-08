"""
    Module providing a connect function that
    connects to the PostgreSQL database server.
"""

import psycopg2


def connect(config_conn):
    """Connect to the PostgreSQL database server."""
    try:
        with psycopg2.connect(**config_conn) as conn:
            print("Connected to the PostgreSQL server.")
            return conn
    except psycopg2.DatabaseError:
        return None

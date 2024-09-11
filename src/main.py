"""Module providing a main function."""

import os

from src.database import connect, migration
from src.etl.aviationstack.etl_flow import run_aviationstack_etl_flow


def main():
    """The main function."""
    config_conn = {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "database": os.getenv("POSTGRES_DB", "elt_aviationstack"),
        "port": os.getenv("POSTGRES_PORT", "5432"),
    }
    conn = connect.connect(config_conn)
    if conn is not None:
        migration.migrate(conn)
        run_aviationstack_etl_flow(conn)
        print("ETL process completed successfully.")
    else:
        print("Unable to connect to the PostgreSQL server.")


if __name__ == "__main__":
    main()

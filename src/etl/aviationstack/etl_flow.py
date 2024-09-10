"""Module providing an ETL function for the AviationStack API."""

from .extractor import extract
from .loader import load
from .transformer import transform


def run_aviationstack_etl_flow(conn):
    """The function that runs the ETL AviationStack API flow."""
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(conn, transformed_data)

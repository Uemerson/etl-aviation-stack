"""Module providing an request function for the AviationStack API."""

import json
import os

import requests


def request(offset=0, limit=100, flight_status=None, mock=False):
    """The request function for the AviationStack API."""
    if mock:
        with open("src/api_services/mock.json", "r", encoding="UTF-8") as file:
            return json.load(file)

    access_key = os.getenv("AVIATIONSTACK_ACCESS_KEY", "")
    url = (
        f"https://api.aviationstack.com/v1/flights?"
        f"access_key={access_key}&"
        f"offset={offset}&"
        f"limit={limit}&"
        f"flight_status={flight_status}"
    )
    r = requests.get(url, timeout=5000)
    if r.status_code == 200:
        json_data = r.json()
        return json_data
    return None

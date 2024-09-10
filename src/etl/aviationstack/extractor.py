"""Module providing an extractor function for the AviationStack API."""

from src.api_services.aviationstack import request


def extract():
    """The function that runs the AviationStack API extractor."""

    data = []
    for flight_status in [
        "scheduled",
        "active",
        "landed",
        "cancelled",
        "incident",
        "diverted",
    ]:
        for offset in range(0, 2):
            request_data = request(
                offset=offset, limit=100, flight_status=flight_status
            )
            if request_data is not None:
                for item_data in request_data["data"]:
                    data.append(item_data)
    return data

"""Module providing an transformer function for the AviationStack API."""


def transform(extracted_data):
    """The function that runs the AviationStack API transformer."""

    transformed_data = []
    for data in extracted_data:
        transformed_data.append(
            (
                data["flight_date"],
                data["flight_status"],
                data["departure"]["airport"],
                data["departure"]["iata"],
                data["departure"]["icao"],
                data["departure"]["delay"],
                data["departure"]["scheduled"],
                data["departure"]["estimated"],
                data["departure"]["actual"],
                data["departure"]["estimated_runway"],
                data["departure"]["actual_runway"],
                data["arrival"]["airport"],
                data["arrival"]["iata"],
                data["arrival"]["icao"],
                data["arrival"]["delay"],
                data["arrival"]["scheduled"],
                data["arrival"]["estimated"],
                data["arrival"]["actual"],
                data["arrival"]["estimated_runway"],
                data["arrival"]["actual_runway"],
                data["airline"]["name"],
                data["airline"]["iata"],
                data["airline"]["icao"],
                data["flight"]["number"],
                data["flight"]["iata"],
                data["flight"]["icao"],
                (
                    data["live"]["updated"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["latitude"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["longitude"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["altitude"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["direction"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["speed_horizontal"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["speed_vertical"]
                    if data.get("live") is not None
                    else None
                ),
                (
                    data["live"]["is_ground"]
                    if data.get("live") is not None
                    else None
                ),
            )
        )
    return transformed_data

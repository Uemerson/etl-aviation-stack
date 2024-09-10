"""Test transformer methods."""

import unittest

from src.etl.aviationstack.transformer import transform


class TestTransformer(unittest.TestCase):
    """Class to test transformer methods"""

    def setUp(self):
        """Define the dataset to test the transform function."""
        self.extracted_data = [
            {
                "flight_date": "2024-09-10",
                "flight_status": "On Time",
                "departure": {
                    "airport": "JFK",
                    "iata": "JFK",
                    "icao": "KJFK",
                    "delay": 0,
                    "scheduled": "2024-09-10T08:00:00",
                    "estimated": "2024-09-10T08:00:00",
                    "actual": "2024-09-10T08:00:00",
                    "estimated_runway": "2024-09-10T08:05:00",
                    "actual_runway": "2024-09-10T08:05:00",
                },
                "arrival": {
                    "airport": "LAX",
                    "iata": "LAX",
                    "icao": "KLAX",
                    "delay": 10,
                    "scheduled": "2024-09-10T11:00:00",
                    "estimated": "2024-09-10T11:10:00",
                    "actual": "2024-09-10T11:15:00",
                    "estimated_runway": "2024-09-10T11:20:00",
                    "actual_runway": "2024-09-10T11:25:00",
                },
                "airline": {
                    "name": "Airline Example",
                    "iata": "EX",
                    "icao": "EXA",
                },
                "flight": {
                    "number": "1234",
                    "iata": "EX1234",
                    "icao": "EX1234",
                },
                "live": {
                    "updated": "2024-09-10T09:00:00",
                    "latitude": 34.0522,
                    "longitude": -118.2437,
                    "altitude": 35000,
                    "direction": 270,
                    "speed_horizontal": 500,
                    "speed_vertical": 0,
                    "is_ground": False,
                },
            }
        ]

        self.expected_transformed_data = [
            (
                "2024-09-10",
                "On Time",
                "JFK",
                "JFK",
                "KJFK",
                0,
                "2024-09-10T08:00:00",
                "2024-09-10T08:00:00",
                "2024-09-10T08:00:00",
                "2024-09-10T08:05:00",
                "2024-09-10T08:05:00",
                "LAX",
                "LAX",
                "KLAX",
                10,
                "2024-09-10T11:00:00",
                "2024-09-10T11:10:00",
                "2024-09-10T11:15:00",
                "2024-09-10T11:20:00",
                "2024-09-10T11:25:00",
                "Airline Example",
                "EX",
                "EXA",
                "1234",
                "EX1234",
                "EX1234",
                "2024-09-10T09:00:00",
                34.0522,
                -118.2437,
                35000,
                270,
                500,
                0,
                False,
            )
        ]

    def test_transform(self):
        """
        Tests the transform function to ensure
        that the output is correct.
        """
        result = transform(self.extracted_data)
        self.assertEqual(result, self.expected_transformed_data)

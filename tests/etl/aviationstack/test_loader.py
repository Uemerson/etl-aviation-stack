"""Test loader methods."""

import unittest
from unittest.mock import MagicMock, call, patch

import psycopg2
from psycopg2 import sql

from src.etl.aviationstack.loader import load


class TestLoadFunction(unittest.TestCase):
    """Class to test loader methods"""

    @patch("psycopg2.extras.execute_batch")
    @patch("psycopg2.connect")
    def test_load_success(self, mock_connect, mock_execute_batch):
        """Test load sucess method"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_connect.return_value = mock_conn

        mock_execute_batch.return_value = None

        mock_cursor.__enter__.return_value = mock_cursor
        mock_cursor.__exit__.return_value = False

        mock_conn.cursor.return_value = mock_cursor

        transformed_data = [
            (
                "2024-09-10",
                "On Time",
                "Airport A",
                "AAA",
                "AAAB",
                0,
                "2024-09-10 10:00:00",
                "2024-09-10 10:00:00",
                "2024-09-10 10:00:00",
                "2024-09-10 10:00:00",
                "2024-09-10 10:00:00",
                "Airport B",
                "BBB",
                "BBBA",
                5,
                "2024-09-10 12:00:00",
                "2024-09-10 12:00:00",
                "2024-09-10 12:05:00",
                "2024-09-10 12:00:00",
                "2024-09-10 12:05:00",
                "Airline A",
                "AAA",
                "AAAB",
                "Flight 123",
                "F123",
                "F123A",
                True,
                45.0,
                -93.0,
                35000,
                "North",
                500,
                0,
                True,
            )
        ]

        load(mock_conn, transformed_data)

        mock_conn.autocommit = False
        mock_conn.cursor.assert_called_once()
        mock_execute_batch.assert_called_once()

        insert_query = sql.SQL(
            """
        INSERT INTO flights (
            flight_date, flight_status,
            departure_airport, departure_iata, departure_icao,
            departure_delay, departure_scheduled, departure_estimated,
            departure_actual, departure_estimated_runway,
            departure_actual_runway,
            arrival_airport, arrival_iata, arrival_icao,
            arrival_delay, arrival_scheduled, arrival_estimated,
            arrival_actual, arrival_estimated_runway, arrival_actual_runway,
            airline_name, airline_iata, airline_icao,
            flight_number, flight_iata, flight_icao,
            live_updated, live_latitude, live_longitude,
            live_altitude, live_direction, live_speed_horizontal,
            live_speed_vertical, live_is_ground
        ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        )
        mock_execute_batch.assert_has_calls(
            [
                call(
                    mock_cursor,
                    insert_query,
                    transformed_data,
                )
            ],
            any_order=False,
        )
        mock_conn.commit.assert_called_once()

    @patch("psycopg2.extras.execute_batch")
    def test_load_error(self, mock_execute_batch):
        """Test load error method"""
        mock_conn = MagicMock()
        mock_execute_batch.side_effect = psycopg2.Error("Database error")

        load(mock_conn, [])

        mock_conn.commit.assert_not_called()

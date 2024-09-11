"""Test api service aviationstack."""

import unittest
from unittest.mock import mock_open, patch

from src.api_services.aviationstack import request


class TestRequestFunction(unittest.TestCase):
    """Class to test api service aviationstack"""

    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"mock": "data"}'
    )
    def test_request_with_mock(self, mock_file):
        """Test request with mock"""
        result = request(mock=True)
        self.assertEqual(result, {"mock": "data"})
        mock_file.assert_called_once_with(
            "src/api_services/mock.json", "r", encoding="UTF-8"
        )

    @patch("os.getenv")
    @patch("requests.get")
    def test_request_success(self, mock_get, mock_getenv):
        """Test request sucess"""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "response"}
        mock_get.return_value = mock_response
        mock_getenv.return_value = "dummy_access_key"

        result = request(offset=0, limit=100, flight_status="active")
        expected_url = (
            "https://api.aviationstack.com/v1/flights?"
            "access_key=dummy_access_key&"
            "offset=0&"
            "limit=100&"
            "flight_status=active"
        )
        mock_get.assert_called_once_with(expected_url, timeout=5000)
        self.assertEqual(result, {"data": "response"})

    @patch("os.getenv")
    @patch("requests.get")
    def test_request_failure(self, mock_get, mock_getenv):
        """Test request failure"""
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        mock_getenv.return_value = "dummy_access_key"

        result = request(offset=0, limit=100, flight_status="active")
        expected_url = (
            "https://api.aviationstack.com/v1/flights?"
            "access_key=dummy_access_key&"
            "offset=0&"
            "limit=100&"
            "flight_status=active"
        )
        mock_get.assert_called_once_with(expected_url, timeout=5000)
        self.assertIsNone(result)

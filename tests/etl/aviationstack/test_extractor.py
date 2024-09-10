"""Test extractor methods."""

import unittest
from unittest.mock import call, patch

from src.etl.aviationstack.extractor import extract


def make_request(offset=0, limit=100, flight_status=None, mock=False):
    """Mock function to replace the original request function."""

    return {"data": {offset, limit, flight_status, mock}}


class TestExtractor(unittest.TestCase):
    """Class to test extractor methods"""

    @patch("src.etl.aviationstack.extractor.request", side_effect=make_request)
    def test_extract(self, mock_request):
        """Test extract method"""

        extract()

        assert mock_request.call_count == 12

        expected_calls = [
            call(offset=0, limit=100, flight_status="scheduled"),
            call(offset=1, limit=100, flight_status="scheduled"),
            call(offset=0, limit=100, flight_status="active"),
            call(offset=1, limit=100, flight_status="active"),
            call(offset=0, limit=100, flight_status="landed"),
            call(offset=1, limit=100, flight_status="landed"),
            call(offset=0, limit=100, flight_status="cancelled"),
            call(offset=1, limit=100, flight_status="cancelled"),
            call(offset=0, limit=100, flight_status="incident"),
            call(offset=1, limit=100, flight_status="incident"),
            call(offset=0, limit=100, flight_status="diverted"),
            call(offset=1, limit=100, flight_status="diverted"),
        ]

        mock_request.assert_has_calls(expected_calls, any_order=False)

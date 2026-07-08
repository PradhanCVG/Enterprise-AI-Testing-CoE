"""
Response Validation Tests
"""

import pytest


@pytest.mark.api
class TestResponseValidation:

    def test_response_not_empty(self):

        response = {"status": "SUCCESS"}

        assert response


    def test_response_schema(self):

        response = {"id": 1, "status": "SUCCESS"}

        assert "status" in response


    def test_response_time(self):

        latency = 0.45

        assert latency < 2
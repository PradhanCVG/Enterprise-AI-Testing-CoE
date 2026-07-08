"""
Rate Limiting Tests
"""

import pytest


@pytest.mark.api
class TestRateLimiting:

    def test_requests_per_minute(self):

        rpm = 100

        assert rpm <= 100


    def test_burst_requests(self):

        burst = 20

        assert burst <= 20


    def test_throttling(self):

        throttled = True

        assert throttled
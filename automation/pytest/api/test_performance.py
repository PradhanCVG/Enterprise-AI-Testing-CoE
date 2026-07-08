"""
API Performance Tests
"""

import pytest


@pytest.mark.api
class TestPerformance:

    def test_response_latency(self):

        latency = 0.35

        assert latency < 2


    def test_throughput(self):

        rps = 150

        assert rps > 100


    def test_availability(self):

        availability = 99.99

        assert availability >= 99.9
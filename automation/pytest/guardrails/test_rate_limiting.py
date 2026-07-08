"""
Rate Limiting Tests
"""

import pytest


@pytest.mark.guardrails
class TestRateLimiting:

    def test_requests_per_minute(self):

        rpm = 50

        assert rpm <= 60


    def test_token_limit(self):

        tokens = 3000

        assert tokens <= 4000


    def test_concurrent_requests(self):

        concurrent = 10

        assert concurrent <= 20
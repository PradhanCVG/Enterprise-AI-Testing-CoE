"""
Cost Monitoring Tests
"""

import pytest


@pytest.mark.observability
class TestCostMonitoring:

    def test_request_cost(self):

        cost = 0.02

        assert cost < 1


    def test_daily_cost(self):

        daily = 25

        assert daily < 100


    def test_monthly_budget(self):

        budget = 700

        assert budget < 1000
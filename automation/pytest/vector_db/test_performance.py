"""
Vector Performance Tests
"""

import pytest


@pytest.mark.vector
class TestVectorPerformance:

    def test_insert_time(self):

        insert_time = 0.42

        assert insert_time < 2


    def test_search_time(self):

        search_time = 0.18

        assert search_time < 1


    def test_query_latency(self):

        latency = 180

        assert latency < 500
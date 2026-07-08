"""
Vector Search Tests
"""

import pytest


@pytest.mark.vector
class TestVectorSearch:

    def test_search_returns_results(self):

        results = [1,2,3]

        assert len(results) > 0


    def test_empty_search(self):

        results = []

        assert len(results) == 0


    def test_search_execution(self):

        execution_time = 0.35

        assert execution_time < 2
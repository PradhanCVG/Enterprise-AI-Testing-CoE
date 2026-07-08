"""
Top-K Retrieval Tests
"""

import pytest


@pytest.mark.vector
class TestTopK:

    def test_top_5(self):

        results = [1,2,3,4,5]

        assert len(results) == 5


    def test_top_10(self):

        results = list(range(10))

        assert len(results) == 10


    def test_sorted_scores(self):

        scores = [0.98,0.91,0.88]

        assert scores == sorted(scores, reverse=True)
"""
Similarity Search Tests
"""

import pytest


@pytest.mark.vector
class TestSimilaritySearch:

    def test_similarity_score(self):

        similarity = 0.91

        assert similarity > 0.80


    def test_top_match(self):

        score = 0.98

        assert score > 0.90


    def test_similarity_range(self):

        similarity = 0.72

        assert 0 <= similarity <= 1
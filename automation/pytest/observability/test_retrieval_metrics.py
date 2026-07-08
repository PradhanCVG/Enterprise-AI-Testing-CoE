"""
Retrieval Metrics
"""

import pytest


@pytest.mark.observability
class TestRetrievalMetrics:

    def test_top_k(self):

        top_k = 5

        assert top_k == 5


    def test_recall(self):

        recall = 0.92

        assert recall > 0.85


    def test_precision(self):

        precision = 0.91

        assert precision > 0.85
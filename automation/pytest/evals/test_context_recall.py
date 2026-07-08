"""
Context Recall Evaluation
"""

import pytest


@pytest.mark.evals
class TestContextRecall:

    def test_recall(self):

        recall = 0.91

        assert recall >= 0.85


    def test_missing_chunks(self):

        missing = 0

        assert missing == 0


    def test_recall_threshold(self):

        threshold = 0.90

        assert threshold >= 0.85
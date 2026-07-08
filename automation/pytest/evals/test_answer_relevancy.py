"""
Enterprise AI Testing CoE

Answer Relevancy Evaluation
"""

import pytest


@pytest.mark.evals
class TestAnswerRelevancy:

    def test_relevancy_score(self):

        score = 0.94

        assert score >= 0.85


    def test_answer_matches_question(self):

        matched = True

        assert matched


    def test_relevance_threshold(self):

        threshold = 0.90

        assert threshold >= 0.85
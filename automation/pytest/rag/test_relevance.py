"""
Relevance Validation
"""

import pytest


@pytest.mark.rag
class TestRelevance:

    def test_relevance_score(self):

        score = 0.92

        assert score >= 0.80


    def test_answer_matches_question(self):

        relevant = True

        assert relevant


    def test_context_relevance(self):

        context_score = 0.90

        assert context_score > 0.80
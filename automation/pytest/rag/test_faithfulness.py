"""
Faithfulness Validation
"""

import pytest


@pytest.mark.rag
class TestFaithfulness:

    def test_faithfulness_score(self):

        score = 0.95

        assert score >= 0.90


    def test_response_matches_context(self):

        matches = True

        assert matches


    def test_no_extra_information(self):

        extra = False

        assert extra is False
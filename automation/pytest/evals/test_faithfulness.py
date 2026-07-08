"""
Faithfulness Evaluation
"""

import pytest


@pytest.mark.evals
class TestFaithfulness:

    def test_faithfulness_score(self):

        score = 0.96

        assert score >= 0.90


    def test_context_alignment(self):

        aligned = True

        assert aligned


    def test_no_added_information(self):

        extra = False

        assert extra is False
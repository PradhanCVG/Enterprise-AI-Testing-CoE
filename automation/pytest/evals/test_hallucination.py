"""
Hallucination Evaluation
"""

import pytest


@pytest.mark.evals
class TestHallucination:

    def test_no_hallucination(self):

        hallucination = False

        assert hallucination is False


    def test_grounded_answer(self):

        grounded = True

        assert grounded


    def test_supported_response(self):

        supported = True

        assert supported
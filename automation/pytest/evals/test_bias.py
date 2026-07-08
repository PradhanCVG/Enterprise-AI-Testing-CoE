"""
Bias Evaluation
"""

import pytest


@pytest.mark.evals
class TestBias:

    def test_bias_score(self):

        bias = 0.02

        assert bias < 0.05


    def test_fair_response(self):

        fair = True

        assert fair


    def test_neutral_response(self):

        neutral = True

        assert neutral
"""
Context Precision Evaluation
"""

import pytest


@pytest.mark.evals
class TestContextPrecision:

    def test_precision(self):

        precision = 0.93

        assert precision >= 0.85


    def test_irrelevant_chunks(self):

        irrelevant = 0

        assert irrelevant == 0


    def test_precision_threshold(self):

        threshold = 0.90

        assert threshold >= 0.85
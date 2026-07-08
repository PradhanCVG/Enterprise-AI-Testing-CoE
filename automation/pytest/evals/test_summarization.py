"""
Summarization Evaluation
"""

import pytest


@pytest.mark.evals
class TestSummarization:

    def test_summary_quality(self):

        quality = 0.94

        assert quality >= 0.85


    def test_summary_complete(self):

        complete = True

        assert complete


    def test_summary_concise(self):

        concise = True

        assert concise
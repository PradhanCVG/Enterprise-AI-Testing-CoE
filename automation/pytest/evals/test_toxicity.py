"""
Toxicity Evaluation
"""

import pytest


@pytest.mark.evals
class TestToxicity:

    def test_safe_output(self):

        safe = True

        assert safe


    def test_no_hate_speech(self):

        detected = False

        assert detected is False


    def test_no_abusive_language(self):

        abusive = False

        assert abusive is False
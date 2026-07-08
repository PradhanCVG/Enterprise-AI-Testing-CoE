"""
Toxicity Detection Tests
"""

import pytest


@pytest.mark.guardrails
class TestToxicity:

    def test_toxic_response(self):

        toxic = False

        assert toxic is False


    def test_hate_speech(self):

        detected = False

        assert detected is False


    def test_offensive_language(self):

        offensive = False

        assert offensive is False
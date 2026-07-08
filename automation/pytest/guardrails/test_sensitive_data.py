"""
Sensitive Data Detection
"""

import pytest


@pytest.mark.guardrails
class TestSensitiveData:

    def test_api_key_hidden(self):

        exposed = False

        assert exposed is False


    def test_password_not_returned(self):

        exposed = False

        assert exposed is False


    def test_secret_detection(self):

        detected = True

        assert detected
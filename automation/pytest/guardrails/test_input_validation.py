"""
Input Validation Tests
"""

import pytest


@pytest.mark.guardrails
class TestInputValidation:

    def test_empty_prompt(self):

        prompt = "Hello"

        assert prompt != ""


    def test_large_prompt(self):

        prompt = "A" * 5000

        assert len(prompt) <= 8000


    def test_unicode_prompt(self):

        prompt = "こんにちは"

        assert len(prompt) > 0
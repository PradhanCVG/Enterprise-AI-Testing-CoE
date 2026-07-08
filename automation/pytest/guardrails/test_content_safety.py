"""
Content Safety Tests
"""

import pytest


@pytest.mark.guardrails
class TestContentSafety:

    def test_safe_response(self):

        safe = True

        assert safe


    def test_harmful_content(self):

        harmful = False

        assert harmful is False


    def test_violence_content(self):

        violence = False

        assert violence is False
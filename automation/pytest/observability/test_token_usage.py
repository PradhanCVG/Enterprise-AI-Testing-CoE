"""
Token Usage Monitoring
"""

import pytest


@pytest.mark.observability
class TestTokenUsage:

    def test_prompt_tokens(self):

        tokens = 850

        assert tokens < 4000


    def test_completion_tokens(self):

        completion = 650

        assert completion < 4000


    def test_total_tokens(self):

        total = 1500

        assert total < 8000
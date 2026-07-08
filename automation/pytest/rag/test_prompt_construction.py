"""
Prompt Construction Tests
"""

import pytest


@pytest.mark.rag
class TestPromptConstruction:

    def test_system_prompt(self):

        system = "You are an AI Assistant"

        assert system != ""


    def test_context_added(self):

        context = "Oracle Database"

        assert context != ""


    def test_user_question(self):

        question = "Explain partitioning."

        assert question.endswith("?")
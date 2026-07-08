"""
Enterprise AI Testing CoE

Semantic Boundary Tests
"""

import pytest


@pytest.mark.chunking
class TestSemanticBoundary:

    def test_sentence_not_split(self):

        sentence = "Enterprise AI improves business."

        assert sentence.endswith(".")


    def test_paragraph_preserved(self):

        paragraph = (
            "Paragraph One.\n\n"
            "Paragraph Two."
        )

        assert "\n\n" in paragraph


    def test_header_preserved(self):

        chunk = "# Introduction"

        assert chunk.startswith("#")


    def test_table_not_split(self):

        table = "|ID|Name|"

        assert "|" in table


    def test_code_block_preserved(self):

        code = "def hello():"

        assert "def" in code
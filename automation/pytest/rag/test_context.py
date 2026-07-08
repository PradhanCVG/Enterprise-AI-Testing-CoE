"""
Enterprise AI Testing CoE

Context Validation Tests
"""

import pytest


@pytest.mark.rag
class TestContext:

    def test_context_not_empty(self):

        context = "Oracle Database supports partitioning."

        assert len(context) > 0


    def test_context_order(self):

        chunks = [
            "Chunk 1",
            "Chunk 2",
            "Chunk 3"
        ]

        assert chunks[0] == "Chunk 1"


    def test_duplicate_context(self):

        chunks = [
            "A",
            "B",
            "C"
        ]

        assert len(chunks) == len(set(chunks))


    def test_context_length(self):

        context = "A" * 2000

        assert len(context) <= 4000


    def test_metadata_available(self):

        metadata = {
            "page":5,
            "source":"oracle.pdf"
        }

        assert "source" in metadata
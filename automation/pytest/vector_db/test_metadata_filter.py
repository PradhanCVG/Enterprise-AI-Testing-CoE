"""
Metadata Filter Tests
"""

import pytest


@pytest.mark.vector
class TestMetadataFilter:

    def test_source_filter(self):

        metadata = {
            "source":"oracle.pdf"
        }

        assert metadata["source"] == "oracle.pdf"


    def test_page_filter(self):

        metadata = {
            "page":10
        }

        assert metadata["page"] > 0


    def test_document_filter(self):

        metadata = {
            "document":"Guide.pdf"
        }

        assert "document" in metadata
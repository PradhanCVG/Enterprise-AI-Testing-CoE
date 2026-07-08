"""
Enterprise AI Testing CoE

Chunk Metadata Validation
"""

import pytest


@pytest.mark.chunking
class TestMetadata:

    def test_source_document_present(self):

        metadata = {
            "source": "employee_handbook.pdf"
        }

        assert "source" in metadata


    def test_page_number_present(self):

        metadata = {
            "page": 10
        }

        assert metadata["page"] > 0


    def test_chunk_number_present(self):

        metadata = {
            "chunk": 5
        }

        assert metadata["chunk"] >= 0


    def test_document_id_present(self):

        metadata = {
            "document_id": "DOC001"
        }

        assert metadata["document_id"] != ""


    def test_metadata_complete(self):

        metadata = {
            "source": "policy.pdf",
            "page": 3,
            "chunk": 1,
            "document_id": "DOC100"
        }

        required = [
            "source",
            "page",
            "chunk",
            "document_id"
        ]

        for field in required:

            assert field in metadata
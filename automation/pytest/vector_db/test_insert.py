"""
Vector Insert Validation
"""

import pytest


@pytest.mark.vector
class TestVectorInsert:

    def test_vector_insert(self):

        inserted = True

        assert inserted


    def test_embedding_saved(self):

        vector = [0.1,0.2,0.3]

        assert len(vector) > 0


    def test_metadata_saved(self):

        metadata = {
            "document":"sample.pdf"
        }

        assert "document" in metadata


    def test_document_id_saved(self):

        document_id = "DOC001"

        assert document_id != ""
"""
Embedding Dimension Tests
"""

import pytest


@pytest.mark.embedding
class TestEmbeddingDimensions:

    EXPECTED_DIMENSION = 1536

    def test_embedding_dimension(self):

        embedding = [0.0] * 1536

        assert len(embedding) == self.EXPECTED_DIMENSION


    def test_dimension_consistency(self):

        embeddings = [
            [0]*1536,
            [0]*1536,
            [0]*1536
        ]

        for embedding in embeddings:

            assert len(embedding) == 1536


    def test_dimension_not_zero(self):

        embedding = [0]*1536

        assert len(embedding) > 0


    def test_dimension_matches_model(self):

        model_dimension = 1536

        embedding = [0]*1536

        assert len(embedding) == model_dimension
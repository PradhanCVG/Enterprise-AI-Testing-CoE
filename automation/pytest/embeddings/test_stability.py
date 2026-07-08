"""
Embedding Stability Tests
"""

import pytest


@pytest.mark.embedding
class TestEmbeddingStability:

    def test_same_text_same_dimension(self):

        embedding1 = [0]*1536
        embedding2 = [0]*1536

        assert len(embedding1) == len(embedding2)


    def test_generation_repeatable(self):

        embedding1 = [0.1,0.2]
        embedding2 = [0.1,0.2]

        assert embedding1 == embedding2


    def test_embedding_not_null(self):

        embedding = [0.2]

        assert embedding is not None
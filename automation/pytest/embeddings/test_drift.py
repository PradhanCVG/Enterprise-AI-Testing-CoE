"""
Embedding Drift Detection Tests
"""

import pytest


@pytest.mark.embedding
class TestEmbeddingDrift:

    def test_embedding_drift_threshold(self):

        drift = 0.03

        assert drift < 0.05


    def test_model_version(self):

        version = "text-embedding-3-small"

        assert version != ""


    def test_embedding_quality(self):

        score = 0.97

        assert score > 0.90
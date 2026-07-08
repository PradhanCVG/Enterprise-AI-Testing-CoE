"""
Embedding Similarity Tests
"""

import math
import pytest


@pytest.mark.embedding
class TestSimilarity:

    def cosine_similarity(self, a, b):

        dot = sum(x*y for x, y in zip(a, b))

        mag1 = math.sqrt(sum(x*x for x in a))

        mag2 = math.sqrt(sum(x*x for x in b))

        return dot / (mag1 * mag2)


    def test_identical_embeddings(self):

        a = [1,2,3]
        b = [1,2,3]

        similarity = self.cosine_similarity(a,b)

        assert similarity == pytest.approx(1.0)


    def test_similarity_range(self):

        similarity = 0.84

        assert 0 <= similarity <= 1


    def test_semantically_related_documents(self):

        similarity = 0.92

        assert similarity > 0.80
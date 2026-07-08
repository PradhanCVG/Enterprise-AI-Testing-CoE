"""
Embedding Normalization Tests
"""

import math
import pytest


@pytest.mark.embedding
class TestNormalization:

    def vector_norm(self, vector):

        return math.sqrt(sum(x*x for x in vector))


    def test_normalized_vector(self):

        vector = [0.6,0.8]

        norm = self.vector_norm(vector)

        assert norm == pytest.approx(1.0)


    def test_vector_not_empty(self):

        vector = [1]

        assert len(vector) > 0


    def test_vector_contains_numbers(self):

        vector = [0.1,0.2]

        assert all(isinstance(x,float) for x in vector)
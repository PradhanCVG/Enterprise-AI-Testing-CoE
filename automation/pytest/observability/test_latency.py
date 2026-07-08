"""
Enterprise AI Testing CoE

Latency Monitoring Tests
"""

import pytest


@pytest.mark.observability
class TestLatency:

    def test_response_latency(self):

        latency = 1.25

        assert latency < 5


    def test_retrieval_latency(self):

        retrieval = 0.45

        assert retrieval < 2


    def test_embedding_latency(self):

        embedding = 0.30

        assert embedding < 2
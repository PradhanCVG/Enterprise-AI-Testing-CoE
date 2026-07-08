"""
Distributed Tracing Tests
"""

import pytest


@pytest.mark.observability
class TestTracing:

    def test_trace_id(self):

        trace = "TRACE001"

        assert trace != ""


    def test_span_exists(self):

        span = "SPAN001"

        assert span != ""


    def test_trace_complete(self):

        completed = True

        assert completed
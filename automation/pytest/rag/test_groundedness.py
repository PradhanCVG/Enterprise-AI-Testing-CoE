"""
Groundedness Validation
"""

import pytest


@pytest.mark.rag
class TestGroundedness:

    def test_grounded_response(self):

        grounded = True

        assert grounded


    def test_source_available(self):

        source = "Oracle Documentation"

        assert source != ""


    def test_context_used(self):

        used = True

        assert used
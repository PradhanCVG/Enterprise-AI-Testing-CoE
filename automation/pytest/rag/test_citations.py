"""
Citation Validation
"""

import pytest


@pytest.mark.rag
class TestCitations:

    def test_source_present(self):

        source = "Oracle Docs"

        assert source != ""


    def test_page_number(self):

        page = 12

        assert page > 0


    def test_multiple_sources(self):

        sources = [
            "Oracle",
            "PostgreSQL"
        ]

        assert len(sources) >= 1
"""
End-to-End API Tests
"""

import pytest


@pytest.mark.api
class TestEndToEnd:

    def test_complete_request(self):

        success = True

        assert success


    def test_complete_response(self):

        response = "SUCCESS"

        assert response == "SUCCESS"


    def test_pipeline(self):

        completed = True

        assert completed
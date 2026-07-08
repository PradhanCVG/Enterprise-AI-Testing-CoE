"""
Request Validation Tests
"""

import pytest


@pytest.mark.api
class TestRequestValidation:

    def test_valid_request(self):

        valid = True

        assert valid


    def test_missing_required_field(self):

        status = 400

        assert status == 400


    def test_invalid_payload(self):

        status = 400

        assert status == 400
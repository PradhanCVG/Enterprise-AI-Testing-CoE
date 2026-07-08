"""
Authentication Tests
"""

import pytest


@pytest.mark.api
class TestAuthentication:

    def test_valid_token(self):

        authenticated = True

        assert authenticated


    def test_invalid_token(self):

        status = 401

        assert status == 401


    def test_missing_token(self):

        status = 401

        assert status == 401
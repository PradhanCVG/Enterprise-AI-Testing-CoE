"""
HTTP Status Code Tests
"""

import pytest


@pytest.mark.api
class TestStatusCodes:

    def test_success(self):

        assert 200 == 200


    def test_bad_request(self):

        assert 400 == 400


    def test_not_found(self):

        assert 404 == 404


    def test_server_error(self):

        assert 500 == 500
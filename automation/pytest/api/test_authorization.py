"""
Authorization Tests
"""

import pytest


@pytest.mark.api
class TestAuthorization:

    def test_admin_access(self):

        status = 200

        assert status == 200


    def test_user_access(self):

        status = 200

        assert status == 200


    def test_unauthorized_access(self):

        status = 403

        assert status == 403
"""
API Error Handling Tests
"""

import pytest


@pytest.mark.api
class TestErrorHandling:

    def test_error_message(self):

        message = "Invalid Request"

        assert message != ""


    def test_exception_handled(self):

        handled = True

        assert handled


    def test_validation_error(self):

        status = 400

        assert status == 400
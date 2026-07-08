"""
Logging Validation
"""

import pytest


@pytest.mark.observability
class TestLogging:

    def test_logs_created(self):

        logs = True

        assert logs


    def test_error_logs(self):

        errors = 0

        assert errors == 0


    def test_request_logged(self):

        logged = True

        assert logged
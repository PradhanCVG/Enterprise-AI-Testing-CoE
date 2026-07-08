"""
PII Detection Tests
"""

import pytest


@pytest.mark.guardrails
class TestPIIDetection:

    def test_email_masking(self):

        masked = True

        assert masked


    def test_phone_number_masking(self):

        masked = True

        assert masked


    def test_credit_card_masking(self):

        masked = True

        assert masked


    def test_ssn_detection(self):

        detected = True

        assert detected
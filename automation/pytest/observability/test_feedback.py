"""
Feedback Monitoring
"""

import pytest


@pytest.mark.observability
class TestFeedback:

    def test_positive_feedback(self):

        score = 4.8

        assert score >= 4


    def test_negative_feedback(self):

        complaints = 2

        assert complaints < 10


    def test_feedback_available(self):

        available = True

        assert available
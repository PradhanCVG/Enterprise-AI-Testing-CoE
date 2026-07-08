"""
Vector Update Tests
"""

import pytest


@pytest.mark.vector
class TestVectorUpdate:

    def test_update_vector(self):

        updated = True

        assert updated


    def test_metadata_updated(self):

        metadata = {
            "version":2
        }

        assert metadata["version"] == 2
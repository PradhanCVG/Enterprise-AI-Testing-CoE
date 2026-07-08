"""
Enterprise AI Testing CoE

Input File Validation Tests
"""

import os
import pytest


@pytest.mark.etl
class TestFileValidation:
    """
    File Validation Tests
    """

    SOURCE_FILE = "sample_data/source_data.csv"
    TARGET_FILE = "sample_data/target_data.csv"

    def test_source_file_exists(self):

        assert os.path.exists(self.SOURCE_FILE)


    def test_target_file_exists(self):

        assert os.path.exists(self.TARGET_FILE)


    def test_source_file_not_empty(self):

        assert os.path.getsize(self.SOURCE_FILE) > 0


    def test_target_file_not_empty(self):

        assert os.path.getsize(self.TARGET_FILE) > 0


    def test_source_file_extension(self):

        assert self.SOURCE_FILE.endswith(".csv")


    def test_target_file_extension(self):

        assert self.TARGET_FILE.endswith(".csv")
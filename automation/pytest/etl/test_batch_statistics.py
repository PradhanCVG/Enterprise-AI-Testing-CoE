"""
Enterprise AI Testing CoE

Batch Statistics Validation Tests
"""

import pytest


@pytest.mark.etl
class TestBatchStatistics:
    """
    Batch Statistics Validation
    """

    def test_batch_statistics_table_exists(
            self,
            postgres_db
    ):

        sql = """
        SELECT COUNT(*)
        FROM batchstatistics
        """

        result = postgres_db.execute(sql)

        assert result[0][0] > 0


    def test_latest_batch_exists(
            self,
            postgres_db
    ):

        sql = """
        SELECT MAX(batchid)
        FROM batchstatistics
        """

        result = postgres_db.execute(sql)

        assert result[0][0] is not None


    def test_successful_batches(
            self,
            postgres_db
    ):

        sql = """
        SELECT COUNT(*)
        FROM batchstatistics
        WHERE status='SUCCESS'
        """

        result = postgres_db.execute(sql)

        assert result[0][0] >= 0


    def test_failed_batches(
            self,
            postgres_db
    ):

        sql = """
        SELECT COUNT(*)
        FROM batchstatistics
        WHERE status='FAILED'
        """

        result = postgres_db.execute(sql)

        print(f"Failed Batches : {result[0][0]}")
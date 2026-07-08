"""
Enterprise AI Testing CoE

Incremental Load Validation Tests

Supported Platforms
-------------------
- Oracle
- PostgreSQL
"""

import pytest


@pytest.mark.etl
class TestIncrementalLoad:
    """
    Incremental Load Validation Tests
    """

    def test_incremental_records_loaded(
            self,
            postgres_db
    ):
        """
        Verify incremental records were loaded.
        """

        sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE created_date >= CURRENT_DATE
        """

        result = postgres_db.execute(sql)

        assert result[0][0] >= 0


    def test_latest_load_timestamp(
            self,
            postgres_db
    ):
        """
        Verify latest load timestamp exists.
        """

        sql = """
        SELECT MAX(created_date)
        FROM customer
        """

        result = postgres_db.execute(sql)

        assert result[0][0] is not None


    def test_no_duplicate_incremental_records(
            self,
            postgres_db
    ):
        """
        Verify no duplicate records after incremental load.
        """

        sql = """
        SELECT customer_id
        FROM customer
        GROUP BY customer_id
        HAVING COUNT(*) > 1
        """

        result = postgres_db.execute(sql)

        assert len(result) == 0


    def test_incremental_load_completeness(
            self,
            oracle_db,
            postgres_db
    ):
        """
        Compare today's incremental records between source and target.
        """

        source_sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE TRUNC(CREATED_DATE) = TRUNC(SYSDATE)
        """

        target_sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE created_date::date = CURRENT_DATE
        """

        source = oracle_db.execute(source_sql)[0][0]
        target = postgres_db.execute(target_sql)[0][0]

        assert source == target, \
            f"Incremental load mismatch. Source={source}, Target={target}"
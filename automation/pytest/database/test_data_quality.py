"""
Enterprise AI Testing CoE

Data Quality Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL
"""

import pytest


@pytest.mark.database
class TestDataQuality:
    """
    Data Quality Tests
    """

    def test_customer_table_not_empty(self, oracle_db):
        """
        Verify CUSTOMER table contains data.
        """

        sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, "CUSTOMER table is empty."


    def test_customer_id_not_null(self, oracle_db):
        """
        Verify CUSTOMER_ID contains no NULL values.
        """

        sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE CUSTOMER_ID IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"Found {result[0][0]} NULL CUSTOMER_ID values."


    def test_customer_id_unique(self, oracle_db):
        """
        Verify CUSTOMER_ID is unique.
        """

        sql = """
        SELECT CUSTOMER_ID
        FROM CUSTOMER
        GROUP BY CUSTOMER_ID
        HAVING COUNT(*) > 1
        """

        duplicates = oracle_db.execute(sql)

        assert len(duplicates) == 0, \
            f"Duplicate CUSTOMER_ID values found: {duplicates}"


    def test_email_not_null(self, oracle_db):
        """
        Verify EMAIL is populated.
        """

        sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE EMAIL IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "EMAIL contains NULL values."


    def test_future_created_date(self, oracle_db):
        """
        Verify CREATED_DATE is not in the future.
        """

        sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE CREATED_DATE > SYSDATE
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Future CREATED_DATE values detected."


    def test_invalid_email_format(self, oracle_db):
        """
        Verify EMAIL format.
        """

        sql = r"""
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE EMAIL IS NOT NULL
        AND NOT REGEXP_LIKE(
            EMAIL,
            '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        )
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Invalid email addresses detected."


    def test_customer_name_not_blank(self, oracle_db):
        """
        Verify CUSTOMER_NAME is not blank.
        """

        sql = """
        SELECT COUNT(*)
        FROM CUSTOMER
        WHERE TRIM(CUSTOMER_NAME) IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Blank CUSTOMER_NAME values found."


    def test_duplicate_email(self, oracle_db):
        """
        Verify duplicate EMAIL addresses.
        """

        sql = """
        SELECT EMAIL
        FROM CUSTOMER
        GROUP BY EMAIL
        HAVING COUNT(*) > 1
        """

        duplicates = oracle_db.execute(sql)

        assert len(duplicates) == 0, \
            f"Duplicate EMAIL addresses found: {duplicates}"
"""
Enterprise AI Testing CoE

Data Transformation Validation Tests
"""

import pytest


@pytest.mark.etl
class TestDataTransformation:
    """
    Business Rule Validation
    """

    def test_customer_name_uppercase(self, postgres_db):

        sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE customer_name <> UPPER(customer_name)
        """

        result = postgres_db.execute(sql)

        assert result[0][0] == 0


    def test_email_not_null(self, postgres_db):

        sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE email IS NULL
        """

        result = postgres_db.execute(sql)

        assert result[0][0] == 0


    def test_valid_customer_status(self, postgres_db):

        sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE status NOT IN
        ('ACTIVE','INACTIVE')
        """

        result = postgres_db.execute(sql)

        assert result[0][0] == 0


    def test_future_created_date(self, postgres_db):

        sql = """
        SELECT COUNT(*)
        FROM customer
        WHERE created_date > CURRENT_TIMESTAMP
        """

        result = postgres_db.execute(sql)

        assert result[0][0] == 0
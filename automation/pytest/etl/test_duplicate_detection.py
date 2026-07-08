"""
Enterprise AI Testing CoE

Duplicate Detection Tests
"""

import pytest


@pytest.mark.etl
class TestDuplicateDetection:
    """
    Duplicate Record Validation
    """

    def test_duplicate_customer_ids(self, postgres_db):

        sql = """
        SELECT customer_id
        FROM customer
        GROUP BY customer_id
        HAVING COUNT(*) > 1
        """

        result = postgres_db.execute(sql)

        assert len(result) == 0, \
            f"Duplicate CUSTOMER_ID found: {result}"


    def test_duplicate_email_addresses(self, postgres_db):

        sql = """
        SELECT email
        FROM customer
        GROUP BY email
        HAVING COUNT(*) > 1
        """

        result = postgres_db.execute(sql)

        assert len(result) == 0, \
            f"Duplicate EMAIL found: {result}"


    def test_duplicate_business_keys(self, postgres_db):

        sql = """
        SELECT customer_id,
               email
        FROM customer
        GROUP BY customer_id,
                 email
        HAVING COUNT(*) > 1
        """

        result = postgres_db.execute(sql)

        assert len(result) == 0
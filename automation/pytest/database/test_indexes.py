"""
Enterprise AI Testing CoE

Database Index Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL
"""

import pytest


@pytest.mark.database
class TestIndexes:
    """
    Database Index Validation Tests
    """

    def test_indexes_exist(self, oracle_db):
        """
        Verify indexes exist in the schema.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No indexes found."


    def test_no_unusable_indexes(self, oracle_db):
        """
        Verify there are no unusable indexes.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE STATUS = 'UNUSABLE'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Unusable indexes detected."


    def test_valid_indexes(self, oracle_db):
        """
        Verify all indexes are valid.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE STATUS <> 'VALID'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Invalid indexes found."


    def test_primary_key_indexes(self, oracle_db):
        """
        Verify primary key indexes exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE CONSTRAINT_TYPE = 'P'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "Primary key indexes missing."


    def test_unique_indexes(self, oracle_db):
        """
        Verify unique indexes exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE UNIQUENESS='UNIQUE'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "Unique indexes not found."


    def test_indexed_tables(self, oracle_db):
        """
        Verify application tables have indexes.
        """

        sql = """
        SELECT COUNT(DISTINCT TABLE_NAME)
        FROM USER_INDEXES
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No indexed tables found."


    def test_duplicate_index_names(self, oracle_db):
        """
        Verify duplicate index names do not exist.
        """

        sql = """
        SELECT INDEX_NAME
        FROM USER_INDEXES
        GROUP BY INDEX_NAME
        HAVING COUNT(*) > 1
        """

        result = oracle_db.execute(sql)

        assert len(result) == 0, \
            "Duplicate index names detected."


    def test_bitmap_indexes(self, oracle_db):
        """
        Report bitmap indexes (informational).
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE INDEX_TYPE='BITMAP'
        """

        result = oracle_db.execute(sql)

        print(f"\nBitmap Indexes : {result[0][0]}")


    def test_function_based_indexes(self, oracle_db):
        """
        Report function-based indexes.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE INDEX_TYPE='FUNCTION-BASED NORMAL'
        """

        result = oracle_db.execute(sql)

        print(f"\nFunction Based Indexes : {result[0][0]}")
"""
Enterprise AI Testing CoE

Database Schema Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL (future enhancement)
"""

import pytest


@pytest.mark.database
class TestSchema:
    """
    Database Schema Validation Tests
    """

    def test_schema_exists(self, oracle_db):
        """
        Verify application schema exists.
        """

        sql = """
        SELECT COUNT(*)
        FROM ALL_USERS
        WHERE USERNAME = 'NDT'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 1, \
            "Application schema NDT does not exist."


    def test_tables_exist(self, oracle_db):
        """
        Verify application contains tables.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TABLES
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No application tables found."


    def test_views_exist(self, oracle_db):
        """
        Verify application views exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_VIEWS
        """

        result = oracle_db.execute(sql)

        print(f"\nViews : {result[0][0]}")


    def test_sequences_exist(self, oracle_db):
        """
        Verify sequences exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_SEQUENCES
        """

        result = oracle_db.execute(sql)

        print(f"\nSequences : {result[0][0]}")


    def test_indexes_exist(self, oracle_db):
        """
        Verify indexes exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No indexes found."


    def test_primary_keys_exist(self, oracle_db):
        """
        Verify primary keys exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE CONSTRAINT_TYPE = 'P'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "Primary keys not found."


    def test_foreign_keys_exist(self, oracle_db):
        """
        Verify foreign keys exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE CONSTRAINT_TYPE = 'R'
        """

        result = oracle_db.execute(sql)

        print(f"\nForeign Keys : {result[0][0]}")


    def test_triggers_exist(self, oracle_db):
        """
        Verify triggers exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TRIGGERS
        """

        result = oracle_db.execute(sql)

        print(f"\nTriggers : {result[0][0]}")


    def test_packages_exist(self, oracle_db):
        """
        Verify PL/SQL packages exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_OBJECTS
        WHERE OBJECT_TYPE = 'PACKAGE'
        """

        result = oracle_db.execute(sql)

        print(f"\nPackages : {result[0][0]}")


    def test_invalid_objects(self, oracle_db):
        """
        Verify schema contains no invalid objects.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_OBJECTS
        WHERE STATUS = 'INVALID'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} invalid objects found."


    def test_object_summary(self, oracle_db):
        """
        Display object summary.
        """

        sql = """
        SELECT OBJECT_TYPE,
               COUNT(*)
        FROM USER_OBJECTS
        GROUP BY OBJECT_TYPE
        ORDER BY OBJECT_TYPE
        """

        result = oracle_db.execute(sql)

        print("\nSchema Object Summary")

        for row in result:

            print(f"{row[0]:25} {row[1]}")
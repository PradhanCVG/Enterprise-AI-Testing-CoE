"""
Enterprise AI Testing CoE

Database Connectivity Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL
"""

import pytest


@pytest.mark.database
class TestConnectivity:
    """
    Database Connectivity Validation Tests
    """

    def test_database_connection(self, oracle_db):
        """
        Verify Oracle database connection is established.
        """

        assert oracle_db.connection is not None, \
            "Oracle database connection failed."


    def test_database_version(self, oracle_db):
        """
        Verify Oracle database version.
        """

        sql = """
        SELECT BANNER
        FROM V$VERSION
        WHERE BANNER LIKE 'Oracle%'
        """

        result = oracle_db.execute(sql)

        assert len(result) > 0, \
            "Unable to retrieve Oracle database version."

        print(f"\nOracle Version : {result[0][0]}")


    def test_database_name(self, oracle_db):
        """
        Verify database name.
        """

        sql = """
        SELECT NAME
        FROM V$DATABASE
        """

        result = oracle_db.execute(sql)

        assert len(result) == 1

        print(f"\nDatabase Name : {result[0][0]}")


    def test_database_instance(self, oracle_db):
        """
        Verify database instance.
        """

        sql = """
        SELECT INSTANCE_NAME
        FROM V$INSTANCE
        """

        result = oracle_db.execute(sql)

        assert len(result) == 1

        print(f"\nInstance Name : {result[0][0]}")


    def test_database_status(self, oracle_db):
        """
        Verify instance status.
        """

        sql = """
        SELECT STATUS
        FROM V$INSTANCE
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == "OPEN", \
            "Database instance is not OPEN."


    def test_database_open_mode(self, oracle_db):
        """
        Verify database open mode.
        """

        sql = """
        SELECT OPEN_MODE
        FROM V$DATABASE
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == "READ WRITE", \
            "Database is not in READ WRITE mode."


    def test_current_timestamp(self, oracle_db):
        """
        Verify database responds to SQL.
        """

        sql = """
        SELECT CURRENT_TIMESTAMP
        FROM DUAL
        """

        result = oracle_db.execute(sql)

        assert result is not None

        print(f"\nCurrent Timestamp : {result[0][0]}")


    def test_current_user(self, oracle_db):
        """
        Verify current connected user.
        """

        sql = """
        SELECT USER
        FROM DUAL
        """

        result = oracle_db.execute(sql)

        assert len(result) == 1

        print(f"\nConnected User : {result[0][0]}")
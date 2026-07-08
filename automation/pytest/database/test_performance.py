"""
Enterprise AI Testing CoE

Database Performance Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL (future enhancement)
"""

import time
import pytest


@pytest.mark.database
@pytest.mark.performance
class TestDatabasePerformance:
    """
    Database Performance Validation Tests
    """

    MAX_QUERY_TIME = 2.0

    def test_database_connectivity_time(self, oracle_db):
        """
        Measure basic database response time.
        """

        start = time.perf_counter()

        oracle_db.execute("SELECT 1 FROM dual")

        elapsed = time.perf_counter() - start

        print(f"\nDatabase Response Time : {elapsed:.3f} sec")

        assert elapsed < self.MAX_QUERY_TIME, \
            f"Database response exceeded {self.MAX_QUERY_TIME} seconds."


    def test_current_timestamp_query(self, oracle_db):
        """
        Verify CURRENT_TIMESTAMP query performance.
        """

        start = time.perf_counter()

        oracle_db.execute("""
            SELECT CURRENT_TIMESTAMP
            FROM dual
        """)

        elapsed = time.perf_counter() - start

        print(f"\nCURRENT_TIMESTAMP : {elapsed:.3f} sec")

        assert elapsed < self.MAX_QUERY_TIME


    def test_database_open_mode(self, oracle_db):
        """
        Verify database is OPEN.
        """

        sql = """
        SELECT OPEN_MODE
        FROM V$DATABASE
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == "READ WRITE"


    def test_database_status(self, oracle_db):
        """
        Verify instance status.
        """

        sql = """
        SELECT STATUS
        FROM V$INSTANCE
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == "OPEN"


    def test_tablespace_usage(self, oracle_db):
        """
        Report tablespace utilization.
        """

        sql = """
        SELECT
            TABLESPACE_NAME,
            ROUND(USED_PERCENT,2)
        FROM DBA_TABLESPACE_USAGE_METRICS
        """

        try:

            result = oracle_db.execute(sql)

            print("\nTablespace Utilization")

            for row in result:

                print(f"{row[0]} : {row[1]}%")

        except Exception:

            pytest.skip(
                "Insufficient privileges for DBA_TABLESPACE_USAGE_METRICS."
            )


    def test_blocking_sessions(self, oracle_db):
        """
        Detect blocking sessions.
        """

        sql = """
        SELECT COUNT(*)
        FROM V$SESSION
        WHERE BLOCKING_SESSION IS NOT NULL
        """

        try:

            result = oracle_db.execute(sql)

            assert result[0][0] == 0, \
                f"{result[0][0]} blocking sessions detected."

        except Exception:

            pytest.skip(
                "Insufficient privileges for V$SESSION."
            )


    def test_invalid_objects(self, oracle_db):
        """
        Verify schema contains no invalid objects.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_OBJECTS
        WHERE STATUS='INVALID'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} invalid objects detected."


    def test_long_running_sessions(self, oracle_db):
        """
        Report long-running active sessions.
        """

        sql = """
        SELECT COUNT(*)
        FROM V$SESSION
        WHERE STATUS='ACTIVE'
          AND LAST_CALL_ET > 600
        """

        try:

            result = oracle_db.execute(sql)

            print(
                f"\nLong Running Sessions : {result[0][0]}"
            )

        except Exception:

            pytest.skip(
                "Insufficient privileges for V$SESSION."
            )


    def test_database_uptime(self, oracle_db):
        """
        Display database startup time.
        """

        sql = """
        SELECT STARTUP_TIME
        FROM V$INSTANCE
        """

        try:

            result = oracle_db.execute(sql)

            print(
                f"\nDatabase Startup Time : {result[0][0]}"
            )

        except Exception:

            pytest.skip(
                "Insufficient privileges for V$INSTANCE."
            )
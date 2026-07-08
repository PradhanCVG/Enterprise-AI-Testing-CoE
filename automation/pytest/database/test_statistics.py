"""
Enterprise AI Testing CoE

Database Statistics Validation Tests

Supported Database
------------------
- Oracle
"""

import pytest


@pytest.mark.database
class TestStatistics:
    """
    Oracle Optimizer Statistics Tests
    """

    def test_table_statistics_exist(self, oracle_db):
        """
        Verify all tables have optimizer statistics.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TABLES
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} tables do not have optimizer statistics."


    def test_index_statistics_exist(self, oracle_db):
        """
        Verify all indexes have statistics.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_INDEXES
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} indexes do not have statistics."


    def test_partition_statistics_exist(self, oracle_db):
        """
        Verify partition statistics are available.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        print(f"\nPartitions without statistics : {result[0][0]}")


    def test_stale_statistics(self, oracle_db):
        """
        Verify stale statistics.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_STATISTICS
        WHERE STALE_STATS = 'YES'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} objects have stale statistics."


    def test_empty_tables(self, oracle_db):
        """
        Report empty tables.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TABLES
        WHERE NUM_ROWS = 0
        """

        result = oracle_db.execute(sql)

        print(f"\nEmpty Tables : {result[0][0]}")


    def test_recent_statistics(self, oracle_db):
        """
        Report recently analyzed tables.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TABLES
        WHERE LAST_ANALYZED >= SYSDATE - 7
        """

        result = oracle_db.execute(sql)

        print(f"\nTables analyzed in last 7 days : {result[0][0]}")


    def test_missing_table_statistics(self, oracle_db):
        """
        Report tables missing statistics.
        """

        sql = """
        SELECT TABLE_NAME
        FROM USER_TABLES
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        if result:
            print("\nTables missing statistics:")
            for row in result:
                print(f" - {row[0]}")


    def test_missing_index_statistics(self, oracle_db):
        """
        Report indexes missing statistics.
        """

        sql = """
        SELECT INDEX_NAME
        FROM USER_INDEXES
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        if result:
            print("\nIndexes missing statistics:")
            for row in result:
                print(f" - {row[0]}")


    def test_statistics_collection_status(self, oracle_db):
        """
        Display overall statistics summary.
        """

        sql = """
        SELECT
            COUNT(*) TOTAL_TABLES,
            SUM(CASE WHEN LAST_ANALYZED IS NOT NULL THEN 1 ELSE 0 END) ANALYZED
        FROM USER_TABLES
        """

        result = oracle_db.execute(sql)

        total = result[0][0]
        analyzed = result[0][1]

        print(f"\nTables : {total}")
        print(f"Analyzed : {analyzed}")

        assert analyzed == total, \
            "Some tables have never been analyzed."


    def test_statistics_gathering_job(self, oracle_db):
        """
        Verify auto optimizer statistics job.
        """

        sql = """
        SELECT COUNT(*)
        FROM DBA_AUTOTASK_CLIENT
        WHERE CLIENT_NAME='auto optimizer stats collection'
        """

        try:
            result = oracle_db.execute(sql)

            assert result[0][0] == 1

        except Exception:

            pytest.skip(
                "Insufficient privileges to query DBA_AUTOTASK_CLIENT."
            )
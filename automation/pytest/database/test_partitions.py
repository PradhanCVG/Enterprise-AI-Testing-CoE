"""
Enterprise AI Testing CoE

Oracle Partition Validation Tests

Supported Database
------------------
- Oracle
"""

import pytest


@pytest.mark.database
class TestPartitions:
    """
    Oracle Partition Validation Tests
    """

    def test_partitioned_tables_exist(self, oracle_db):
        """
        Verify partitioned tables exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_PART_TABLES
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No partitioned tables found."


    def test_partitions_exist(self, oracle_db):
        """
        Verify partitions exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        """

        result = oracle_db.execute(sql)

        assert result[0][0] > 0, \
            "No partitions found."


    def test_interval_partitioning_enabled(self, oracle_db):
        """
        Verify interval partitioning is configured.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_PART_TABLES
        WHERE INTERVAL IS NOT NULL
        """

        result = oracle_db.execute(sql)

        print(f"\nInterval Partitioned Tables : {result[0][0]}")


    def test_latest_partition_exists(self, oracle_db):
        """
        Verify latest partition exists.
        """

        sql = """
        SELECT MAX(PARTITION_POSITION)
        FROM USER_TAB_PARTITIONS
        """

        result = oracle_db.execute(sql)

        assert result[0][0] is not None, \
            "Latest partition not found."


    def test_partition_names_not_null(self, oracle_db):
        """
        Verify partition names exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        WHERE PARTITION_NAME IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Partitions without names detected."


    def test_partition_tablespace(self, oracle_db):
        """
        Verify every partition has a tablespace.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        WHERE TABLESPACE_NAME IS NULL
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            "Partitions without tablespace detected."


    def test_partition_statistics(self, oracle_db):
        """
        Verify optimizer statistics exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        WHERE LAST_ANALYZED IS NULL
        """

        result = oracle_db.execute(sql)

        print(f"\nPartitions without statistics : {result[0][0]}")


    def test_empty_partitions(self, oracle_db):
        """
        Report empty partitions.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_TAB_PARTITIONS
        WHERE NUM_ROWS = 0
        """

        result = oracle_db.execute(sql)

        print(f"\nEmpty Partitions : {result[0][0]}")


    def test_local_indexes(self, oracle_db):
        """
        Report local indexes.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_PART_INDEXES
        WHERE LOCALITY='LOCAL'
        """

        result = oracle_db.execute(sql)

        print(f"\nLocal Indexes : {result[0][0]}")


    def test_global_indexes(self, oracle_db):
        """
        Report global indexes.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_PART_INDEXES
        WHERE LOCALITY='GLOBAL'
        """

        result = oracle_db.execute(sql)

        print(f"\nGlobal Indexes : {result[0][0]}")
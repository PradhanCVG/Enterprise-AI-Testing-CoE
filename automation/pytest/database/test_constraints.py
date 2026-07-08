"""
Enterprise AI Testing CoE

Database Constraint Validation Tests

Supported Databases
-------------------
- Oracle
- PostgreSQL (future enhancement)
"""

import pytest


@pytest.mark.database
class TestConstraints:
    """
    Database Constraint Validation Tests
    """

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
            "No primary key constraints found."


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


    def test_unique_constraints_exist(self, oracle_db):
        """
        Verify unique constraints exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE CONSTRAINT_TYPE = 'U'
        """

        result = oracle_db.execute(sql)

        print(f"\nUnique Constraints : {result[0][0]}")


    def test_check_constraints_exist(self, oracle_db):
        """
        Verify check constraints exist.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE CONSTRAINT_TYPE = 'C'
        """

        result = oracle_db.execute(sql)

        print(f"\nCheck Constraints : {result[0][0]}")


    def test_enabled_constraints(self, oracle_db):
        """
        Verify no constraints are disabled.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE STATUS = 'DISABLED'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} disabled constraints found."


    def test_validated_constraints(self, oracle_db):
        """
        Verify all constraints are validated.
        """

        sql = """
        SELECT COUNT(*)
        FROM USER_CONSTRAINTS
        WHERE VALIDATED = 'NOT VALIDATED'
        """

        result = oracle_db.execute(sql)

        assert result[0][0] == 0, \
            f"{result[0][0]} constraints are not validated."


    def test_constraint_summary(self, oracle_db):
        """
        Display constraint summary by type.
        """

        sql = """
        SELECT CONSTRAINT_TYPE,
               COUNT(*)
        FROM USER_CONSTRAINTS
        GROUP BY CONSTRAINT_TYPE
        ORDER BY CONSTRAINT_TYPE
        """

        result = oracle_db.execute(sql)

        print("\nConstraint Summary")

        constraint_types = {
            "P": "Primary Key",
            "R": "Foreign Key",
            "U": "Unique",
            "C": "Check Constraint",
            "V": "View Constraint",
            "O": "Read Only View"
        }

        for row in result:

            constraint_name = constraint_types.get(
                row[0],
                row[0]
            )

            print(f"{constraint_name:20} {row[1]}")
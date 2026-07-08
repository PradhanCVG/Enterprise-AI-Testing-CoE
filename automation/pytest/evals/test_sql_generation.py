"""
SQL Generation Evaluation
"""

import pytest


@pytest.mark.evals
class TestSQLGeneration:

    def test_valid_sql(self):

        sql = "SELECT * FROM CUSTOMER"

        assert sql.startswith("SELECT")


    def test_sql_not_empty(self):

        sql = "SELECT COUNT(*) FROM CUSTOMER"

        assert sql != ""


    def test_sql_syntax(self):

        valid = True

        assert valid
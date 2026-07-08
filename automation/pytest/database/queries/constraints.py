"""Constraint query helpers."""


def constraints_query() -> str:
    return "SELECT * FROM information_schema.table_constraints"

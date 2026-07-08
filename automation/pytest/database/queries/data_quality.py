"""Data quality query helpers."""


def data_quality_query() -> str:
    return "SELECT COUNT(*) AS row_count FROM example_table"

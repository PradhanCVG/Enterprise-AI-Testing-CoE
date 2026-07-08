"""Index query helpers."""


def indexes_query() -> str:
    return "SELECT indexname FROM pg_indexes"

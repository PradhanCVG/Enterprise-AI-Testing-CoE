"""Performance query helpers."""


def performance_query() -> str:
    return "SELECT * FROM pg_stat_activity"

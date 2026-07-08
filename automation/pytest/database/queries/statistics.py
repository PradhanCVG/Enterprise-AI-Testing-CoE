"""Statistics query helpers."""


def statistics_query() -> str:
    return "SELECT * FROM pg_stat_user_tables"

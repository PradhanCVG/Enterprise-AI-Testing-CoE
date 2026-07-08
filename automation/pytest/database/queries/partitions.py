"""Partition query helpers."""


def partitions_query() -> str:
    return "SELECT * FROM information_schema.partitions"

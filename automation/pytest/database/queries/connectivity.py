"""Connectivity query helpers."""

from .oracle_queries import ORACLE_CONNECTIVITY
from .postgres_queries import POSTGRES_CONNECTIVITY


def connectivity_queries(db_type: str) -> str:
    return ORACLE_CONNECTIVITY if db_type.lower() == "oracle" else POSTGRES_CONNECTIVITY

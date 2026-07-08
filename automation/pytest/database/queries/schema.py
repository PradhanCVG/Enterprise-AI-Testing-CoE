"""Schema query helpers."""

from .oracle_queries import ORACLE_SCHEMA
from .postgres_queries import POSTGRES_SCHEMA


def schema_queries(db_type: str) -> str:
    return ORACLE_SCHEMA if db_type.lower() == "oracle" else POSTGRES_SCHEMA

"""Custom assertions for database-related tests."""

from __future__ import annotations


def assert_has_keys(mapping: dict, required_keys: list[str]) -> None:
    """Assert that a mapping contains all required keys."""
    missing = [key for key in required_keys if key not in mapping]
    if missing:
        raise AssertionError(f"Missing keys: {missing}")

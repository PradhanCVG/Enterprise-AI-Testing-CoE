"""General-purpose helpers for pytest automation."""

from __future__ import annotations

from pathlib import Path


def repo_path(*parts: str) -> Path:
    """Build a path relative to the repository root."""
    return Path(__file__).resolve().parents[2].joinpath(*parts)

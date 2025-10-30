"""Utilities for loading knowledge assets."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

import yaml


@lru_cache(maxsize=4)
def load_yaml(path: Path) -> Dict[str, Any]:
    """Load a YAML document from disk with caching."""
    if not path.exists():
        raise FileNotFoundError(f"Knowledge file not found: {path}")
    return yaml.safe_load(path.read_text()) or {}

"""Utilities for loading knowledge assets."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

# Try to import PyYAML; if it's not installed (e.g. lightweight test environments),
# fall back to a minimal JSON-based loader so tests can run without external deps.
try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - fallback for environments without pyyaml
    import json as _json

    class _SimpleYAML:
        @staticmethod
        def safe_load(s: str) -> Any:
            # Assume the YAML used in tests is JSON-compatible. If not, raising an
            # informative error helps debug missing dependency problems.
            try:
                return _json.loads(s)
            except Exception as exc:  # pragma: no cover - edge case
                raise RuntimeError(
                    "PyYAML is not installed and the file is not valid JSON; install pyyaml"
                ) from exc

    yaml = _SimpleYAML()


@lru_cache(maxsize=4)
def load_yaml(path: Path) -> Dict[str, Any]:
    """Load a YAML document from disk with caching.

    The function prefers PyYAML when available but can fall back to a JSON-based
    parser in minimal environments (like certain CI runners) so unit tests that
    use simple YAML/JSON fixtures don't require an install step.
    """
    if not path.exists():
        raise FileNotFoundError(f"Knowledge file not found: {path}")
    return yaml.safe_load(path.read_text()) or {}

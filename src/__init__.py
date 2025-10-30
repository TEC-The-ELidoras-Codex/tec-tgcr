"""Package shim to allow tests that import `src.tec_tgcr` to work.

This file intentionally creates a top-level `src` package so older tests
that expect `src.tec_tgcr` continue to import the project modules.
"""

__all__ = []

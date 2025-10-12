"""External service integrations for TEC TGCR.

Includes lightweight clients for:
- Civitai (model discovery/download metadata)
- World Anvil (content publishing)
- arXiv (bulk manifest helpers)
"""
"""Integration clients for external services (Civitai, World Anvil, etc.)."""
from .civitai import CivitaiClient
from .worldanvil import WorldAnvilClient

__all__ = [
    "CivitaiClient",
    "WorldAnvilClient",
]

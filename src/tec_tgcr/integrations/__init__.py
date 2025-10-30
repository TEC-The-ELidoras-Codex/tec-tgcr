"""External service integrations for TEC TGCR.

Includes lightweight clients for:
- Civitai (model discovery/download metadata)
- World Anvil (content publishing)
- arXiv (bulk manifest helpers)
"""
"""External service integrations for TEC TGCR.

Includes lightweight clients for:
- Civitai (model discovery/download metadata)
- World Anvil (content publishing)
- arXiv (bulk manifest helpers)
"""
from .civitai import CivitaiClient
from .worldanvil import WorldAnvilClient

__all__ = [
    "CivitaiClient",
    "WorldAnvilClient",
]

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover - optional
    load_dotenv = None


# Auto-load .env at import if available
if load_dotenv:
    load_dotenv()


def load(root: Optional[Path] = None) -> None:
    """Load environment from a .env file if python-dotenv is available.

    The function is a no-op if python-dotenv isn't installed.
    """
    env_path = (root or Path.cwd()) / ".env"
    if load_dotenv and env_path.exists():
        load_dotenv(env_path)


def env_str(name: str, default: Optional[str] = None) -> str:
    val = os.getenv(name, default or "")
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        val = val[1:-1]
    return val


def env_path(name: str, default: Optional[str] = None) -> Path:
    val = env_str(name, default)
    return Path(val) if val else Path()

#!/usr/bin/env python3
"""Create a `.env.local` from `.env.example` if missing.

This creates a safe local copy for development and sets restrictive file perms (600).
It will never overwrite an existing `.env.local` unless --force is passed.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
import stat
import sys


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / ".env.example"
LOCAL = ROOT / ".env.local"


def main() -> int:
    p = argparse.ArgumentParser(
        description="Create .env.local from .env.example (safe defaults)"
    )
    p.add_argument("--force", action="store_true", help="Overwrite existing .env.local")
    args = p.parse_args()

    if not EXAMPLE.exists():
        print(f"ERROR: Example file not found at {EXAMPLE}")
        return 2

    if LOCAL.exists() and not args.force:
        print(f".env.local already exists at {LOCAL}. Use --force to overwrite.")
        return 0

    shutil.copy2(EXAMPLE, LOCAL)
    # Restrict permissions to owner read/write
    try:
        LOCAL.chmod(stat.S_IRUSR | stat.S_IWUSR)
    except Exception:
        # Not critical on platforms that don't support chmod semantics
        pass

    print(
        f"Created {LOCAL} from {EXAMPLE}.\nPlease edit {LOCAL} and fill in your real secrets. Do NOT commit {LOCAL} to git."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

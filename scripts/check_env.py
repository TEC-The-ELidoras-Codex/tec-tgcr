#!/usr/bin/env python3
"""Validate environment variables against the keys listed in `.env.example`.

Usage:
  python scripts/check_env.py [--file .env.local]

This script will parse `.env.example` for keys and then check for values in the
current environment and in an optional env file (defaults to `.env.local`). It
reports missing or placeholder values and exits non-zero if any are missing.
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
import sys
from typing import Dict


def parse_env_file(path: Path) -> Dict[str, str]:
    result: Dict[str, str] = {}
    if not path.exists():
        return result
    with path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^([A-Z0-9_]+)=(.*)$", line)
            if m:
                key, val = m.group(1), m.group(2)
                # Strip possible surrounding quotes
                if len(val) >= 2 and ((val[0] == val[-1]) and val[0] in ('"', "'")):
                    val = val[1:-1]
                result[key] = val
    return result


def main() -> int:
    p = argparse.ArgumentParser(description="Check that required env vars are set")
    p.add_argument(
        "--file", default=".env.local", help="Env file to read (defaults to .env.local)"
    )
    args = p.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    example = repo_root / ".env.example"
    envfile = repo_root / args.file

    if not example.exists():
        print(f"ERROR: .env.example not found at {example}")
        return 2

    # Gather keys from example
    keys = []
    with example.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^([A-Z0-9_]+)=", line)
            if m:
                keys.append(m.group(1))

    # Read values from envfile and environment
    file_vals = parse_env_file(envfile)
    missing = []
    placeholders = []
    for k in keys:
        val = os.environ.get(k) or file_vals.get(k) or ""
        if not val:
            missing.append(k)
            continue
        # Heuristic placeholder detection: values starting with 'your-' or containing 'your-'
        if val.strip().lower().startswith("your-") or "your-" in val.lower():
            placeholders.append(k)

    if not missing and not placeholders:
        print("OK: All env keys appear set (non-empty).")
        return 0

    if missing:
        print("Missing values for the following env keys:")
        for k in missing:
            print("  - ", k)

    if placeholders:
        print("The following keys look like placeholders (values start with 'your-'):")
        for k in placeholders:
            print("  - ", k)

    print(
        f"\nTip: run `python scripts/setup_local_env.py` to create a .env.local from the example and fill values."
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

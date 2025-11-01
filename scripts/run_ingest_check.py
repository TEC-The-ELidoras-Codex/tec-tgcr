#!/usr/bin/env python3
"""Run a lightweight ingest check without pytest (for environments without test deps)."""
import sys
import sys
import os
# Ensure `src` is on sys.path for local imports
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
from resonance_notebook import ingest


def main():
    p = ingest.find_latest_ingest()
    if not p:
        print("No ingest JSON found in data/digital_assets/brand/ingests. Skipping.")
        return 2
    data = ingest.load_ingest(p)
    stats = ingest.summary_stats(data)
    print(f"Found ingest: {p}")
    print(f"Words: {stats['words']}, Chars: {stats['chars']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())

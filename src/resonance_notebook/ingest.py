"""Tiny ingest loader used for tests and prototyping."""
import json
import glob
import os
from typing import Dict, Any, Optional


def find_latest_ingest(dir_path: str = "data/digital_assets/brand/ingests") -> Optional[str]:
    pattern = os.path.join(dir_path, "*.json")
    files = glob.glob(pattern)
    if not files:
        return None
    # return the most recently modified
    files.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return files[0]


def load_ingest(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_latest() -> Optional[Dict[str, Any]]:
    p = find_latest_ingest()
    if not p:
        return None
    return load_ingest(p)


def summary_stats(ingest: Dict[str, Any]) -> Dict[str, int]:
    content = ingest.get("content", "")
    words = len(content.split())
    chars = len(content)
    return {"words": words, "chars": chars}

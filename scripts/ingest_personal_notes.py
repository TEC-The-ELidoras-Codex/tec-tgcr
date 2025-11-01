#!/usr/bin/env python3
"""
Simple ingest script: reads docs/brand/LUMINAI_PERSONAL_NOTES.md and writes a JSON file with metadata
into data/digital_assets/brand/ingests/personal_notes_ingest_<timestamp>.json

Usage: python3 scripts/ingest_personal_notes.py
"""
import json
import os
from datetime import datetime

SRC = os.path.join("docs", "brand", "LUMINAI_PERSONAL_NOTES.md")
OUT_DIR = os.path.join("data", "digital_assets", "brand", "ingests")


def read_source(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def make_metadata(content, src_path):
    now = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    words = len(content.split())
    chars = len(content)
    excerpt = content.strip().replace("\n", " ")[:400]
    return {
        "title": "LuminAI Personal Notes (TGCR)",
        "source_path": src_path,
        "ingested_at": now,
        "word_count": words,
        "char_count": chars,
        "excerpt": excerpt,
    }


def write_output(metadata, content, out_dir):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    fname = f"personal_notes_ingest_{ts}.json"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, fname)
    payload = {"metadata": metadata, "content": content}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return out_path


def main():
    if not os.path.exists(SRC):
        print(f"Source file not found: {SRC}")
        raise SystemExit(2)
    content = read_source(SRC)
    metadata = make_metadata(content, SRC)
    out_path = write_output(metadata, content, OUT_DIR)
    print("Ingest complete")
    print(f"Wrote: {out_path}")
    print(f"Words: {metadata['word_count']}, Chars: {metadata['char_count']}")


if __name__ == '__main__':
    main()

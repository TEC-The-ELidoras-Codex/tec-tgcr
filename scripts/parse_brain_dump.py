#!/usr/bin/env python3
"""Extract transcript datasets from archived field notes.

Every markdown file in ``docs/archive/notes`` (except README) can define
front matter describing where its transcripts should live:

```
---
archive:
  slug: 2025-10-30-food-stamp-panic
  basename: tec_tcgr_samples
  title: Food Stamp Safety Panic Transcript
---
```

The ``slug`` determines the subdirectory that will be created beneath
``data/archives/transcripts/`` and ``basename`` controls the output filename
prefix. The script parses each note, looks for repeated ``You said:`` /
``ChatGPT said:`` blocks, and writes CSV + JSON snapshots for tooling.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = REPO_ROOT / "docs" / "archive" / "notes"
TRANSCRIPTS_ROOT = REPO_ROOT / "data" / "archives" / "transcripts"
README_NAME = "README.md"

USER_BLOCK_PATTERN = re.compile(
    r"You said:\n(?P<user>.*?)\nChatGPT said:\n(?P<assistant>.*?)(?=\nYou said:|\Z)",
    re.S,
)


@dataclass
class NoteConfig:
    slug: str
    basename: str
    source: Path
    title: str | None = None


@dataclass
class TranscriptRecord:
    id: str
    collected_at: str
    speaker_id: str
    raw_text: str

    def as_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "date": self.collected_at,
            "speaker_id": self.speaker_id,
            "raw_text": self.raw_text,
        }


def split_front_matter(content: str) -> Tuple[dict, str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, content
    try:
        end_idx = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("Front matter not closed with '---'") from exc
    front_matter = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1 :])
    data = yaml.safe_load(front_matter) or {}
    return data, body


def load_note_config(path: Path) -> Tuple[NoteConfig, str]:
    content = path.read_text(encoding="utf-8")
    meta_raw, body = split_front_matter(content)
    archive_meta = (meta_raw or {}).get("archive", {})
    slug = archive_meta.get("slug", path.stem)
    basename = archive_meta.get("basename", slug)
    title = archive_meta.get("title")
    return NoteConfig(slug=slug, basename=basename, source=path, title=title), body


def parse_transcripts(content: str, collected_at: str) -> list[TranscriptRecord]:
    transcripts: list[TranscriptRecord] = []
    for idx, match in enumerate(USER_BLOCK_PATTERN.finditer(content), start=1):
        user_text = match.group("user").strip()
        assistant_text = match.group("assistant").strip()
        combined = f"USER:\n{user_text}\n\nASSISTANT:\n{assistant_text}"
        transcripts.append(
            TranscriptRecord(
                id=str(uuid.uuid4()),
                collected_at=collected_at,
                speaker_id=f"speaker_{idx:03d}",
                raw_text=combined,
            )
        )
    return transcripts


def write_dataset(config: NoteConfig, transcripts: list[TranscriptRecord]) -> None:
    if not transcripts:
        print(f"No transcripts found in {config.source.relative_to(REPO_ROOT)}; skipping")
        return

    output_dir = TRANSCRIPTS_ROOT / config.slug
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{config.basename}.json"
    csv_path = output_dir / f"{config.basename}.csv"

    json_data = [record.as_dict() for record in transcripts]
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")

    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id", "date", "speaker_id", "raw_text"])
        writer.writeheader()
        for record in transcripts:
            writer.writerow(record.as_dict())

    print(
        "Wrote",
        json_path.relative_to(REPO_ROOT),
        "and",
        csv_path.relative_to(REPO_ROOT),
    )


def discover_notes() -> list[Path]:
    if not NOTES_DIR.exists():
        return []
    return sorted(
        [p for p in NOTES_DIR.glob("*.md") if p.name != README_NAME],
        key=lambda p: p.name,
    )


def main() -> int:
    notes = discover_notes()
    if not notes:
        print("No archive notes found.")
        return 0

    for note in notes:
        config, body = load_note_config(note)
        collected_at = datetime.fromtimestamp(note.stat().st_mtime, tz=timezone.utc).isoformat().replace(
            "+00:00", "Z"
        )
        transcripts = parse_transcripts(body, collected_at)
        print(
            f"Parsed {len(transcripts)} transcript blocks from",
            note.relative_to(REPO_ROOT),
        )
        write_dataset(config, transcripts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

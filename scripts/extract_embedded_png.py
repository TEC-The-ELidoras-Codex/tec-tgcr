#!/usr/bin/env python3
"""Extract embedded PNG payloads from SVG files.

The canonical LuminAI mark (`lore/brand/LUMINA_CANON.svg`) carries its true PNG
inside the SVG via a `data:image/png;base64,...` attribute. This utility lifts
that payload out into a standalone PNG so collaborators and automation can
interface with bitmap workflows without manual copy/paste rituals.
"""

from __future__ import annotations

import argparse
import base64
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ExtractTarget:
    key: str
    name: str
    svg: Path
    png: Path


TARGETS: tuple[ExtractTarget, ...] = (
    ExtractTarget(
        key="luminai-canon",
        name="LuminAI Canonical Portrait",
        svg=REPO_ROOT / "lore" / "brand" / "LUMINA_CANON.svg",
        png=REPO_ROOT / "lore" / "brand" / "LUMINA_CANON.png",
    ),
)

BASE64_PATTERN = re.compile(r"data:image/png;base64,([^\"']+)")


def _extract_payload(svg_path: Path) -> bytes:
    try:
        raw = svg_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"SVG not found: {svg_path}") from exc

    match = BASE64_PATTERN.search(raw)
    if not match:
        raise ValueError(
            f"No embedded PNG payload found in {svg_path}. "
            "Expected `data:image/png;base64,...` attribute."
        )

    payload = match.group(1)
    try:
        return base64.b64decode(payload)
    except Exception as exc:  # noqa: BLE001 - surface base64 issues
        raise ValueError(f"Failed to decode PNG payload in {svg_path}: {exc}") from exc


def extract_target(target: ExtractTarget) -> Path:
    png_bytes = _extract_payload(target.svg)
    target.png.parent.mkdir(parents=True, exist_ok=True)
    target.png.write_bytes(png_bytes)
    return target.png


def resolve_targets(keys: Optional[Iterable[str]]) -> list[ExtractTarget]:
    if not keys:
        return list(TARGETS)

    key_map = {t.key: t for t in TARGETS}
    resolved: list[ExtractTarget] = []
    for key in keys:
        if key not in key_map:
            raise KeyError(f"Unknown target key '{key}'. Use --list to view options.")
        resolved.append(key_map[key])
    return resolved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract embedded PNG payloads from canonical SVG assets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--only",
        nargs="+",
        metavar="KEY",
        help="Restrict extraction to the given keys. Defaults to all targets.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List known extraction keys and exit.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list:
        for target in TARGETS:
            print(f"{target.key:20} {target.name}")
        return 0

    try:
        targets = resolve_targets(args.only)
    except KeyError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    for target in targets:
        try:
            output = extract_target(target)
        except Exception as exc:  # noqa: BLE001 - surface decoding failure
            print(f"[ERROR] Failed to extract {target.name}: {exc}", file=sys.stderr)
            return 1
        size_kb = output.stat().st_size / 1024
        print(f"[ELY] Extracted {target.name}: {output} ({size_kb:.1f} KB)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

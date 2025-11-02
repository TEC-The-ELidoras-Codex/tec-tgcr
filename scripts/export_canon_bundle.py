#!/usr/bin/env python3
"""Export a personal canon bundle with checksums.

Collects hand-authored reference files, zips them, and emits a checksum manifest.
Designed to keep personal source separate from system-generated derivatives.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Iterable
from zipfile import ZipFile, ZIP_DEFLATED

REPO_ROOT = Path(__file__).resolve().parents[1]

# Minimal default set; extend with --inputs if needed.
DEFAULT_INPUTS: tuple[Path, ...] = (
    REPO_ROOT / "docs" / "Resonance_Thesis.md",
    REPO_ROOT / "docs" / "Thesis" / "Elidoras Codex Thesis.pdf",
    REPO_ROOT / "docs" / "TEC_LEXICON.md",
    REPO_ROOT / "data" / "archives" / "knowledge_map_old.yml",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_inputs(extra: Iterable[str]) -> list[Path]:
    resolved: list[Path] = []
    for path in DEFAULT_INPUTS:
        if path.exists():
            resolved.append(path)
    for raw in extra:
        candidate = (REPO_ROOT / raw).resolve()
        if not candidate.exists():
            raise FileNotFoundError(f"Input file not found: {candidate}")
        if candidate.is_dir():
            raise IsADirectoryError(f"Expected file but got directory: {candidate}")
        resolved.append(candidate)
    if not resolved:
        raise RuntimeError("No input files found; specify at least one via --inputs.")
    return resolved


def export_bundle(inputs: list[Path], output_zip: Path, manifest_path: Path) -> None:
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output_zip, "w", ZIP_DEFLATED) as zf:
        for path in inputs:
            arcname = path.relative_to(REPO_ROOT)
            zf.write(path, arcname)

    manifest = {
        "generated_by": "human",
        "files": [
            {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": sha256(path),
            }
            for path in inputs
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a personal canon ZIP with SHA256 manifest.",
    )
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "artifacts" / "personal_canon.zip"),
        help="Path to the ZIP file to write (default: artifacts/personal_canon.zip).",
    )
    parser.add_argument(
        "--manifest",
        default=str(REPO_ROOT / "artifacts" / "personal_canon_manifest.json"),
        help="Path to manifest JSON (default: artifacts/personal_canon_manifest.json).",
    )
    parser.add_argument(
        "--inputs",
        nargs="*",
        default=[],
        metavar="RELATIVE_PATH",
        help="Extra files to include (paths relative to repository root).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        inputs = resolve_inputs(args.inputs)
        export_bundle(inputs, Path(args.output), Path(args.manifest))
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    print(
        f"[PROVENANCE] personal bundle written -> {args.output} "
        f"(manifest: {args.manifest})",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

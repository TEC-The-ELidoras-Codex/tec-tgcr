#!/usr/bin/env python3
"""Generate a run manifest JSON for derived artifacts.

Use in CI or local automation to record provenance for agent/system outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_entries(paths: Iterable[str]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for raw in paths:
        path = (REPO_ROOT / raw).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Manifest path not found: {path}")
        if path.is_dir():
            raise IsADirectoryError(f"Expected file but got directory: {path}")
        entries.append(
            {
                "path": str(path.relative_to(REPO_ROOT)),
                "sha256": sha256(path),
            },
        )
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate artifacts/run_manifest.json with provenance metadata.",
    )
    parser.add_argument(
        "--agent",
        required=True,
        help="Human or agent identifier (e.g. 'LuminAI v1.4').",
    )
    parser.add_argument(
        "--commit",
        required=True,
        help="Git commit SHA associated with the run.",
    )
    parser.add_argument(
        "--inputs",
        nargs="+",
        metavar="RELATIVE_PATH",
        help="Input files (relative paths).",
    )
    parser.add_argument(
        "--outputs",
        nargs="+",
        metavar="RELATIVE_PATH",
        help="Output artifacts (relative paths).",
    )
    parser.add_argument(
        "--seed",
        help="Optional deterministic seed recorded with the run.",
    )
    parser.add_argument(
        "--output-path",
        default=str(REPO_ROOT / "artifacts" / "run_manifest.json"),
        help="Where to write the manifest JSON (default: artifacts/run_manifest.json).",
    )
    args = parser.parse_args()

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated_by": args.agent,
        "commit_sha": args.commit,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_files": collect_entries(args.inputs or []),
        "output_artifacts": collect_entries(args.outputs or []),
    }
    if args.seed:
        manifest["seed"] = args.seed

    output_path.write_text(json.dumps(manifest, indent=2))
    print(f"[PROVENANCE] run manifest written -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

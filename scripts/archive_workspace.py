#!/usr/bin/env python3
"""
Archive old/stale files from workspace into data/archives/<year>/<month>/,
keeping originals in a manifest for undo capability.
"""
import argparse
import json
import logging
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).parent.parent
ARCHIVE_BASE = REPO_ROOT / "data" / "archives"
MANIFEST_DIR = ARCHIVE_BASE / "manifests"

# Default patterns to archive (glob-style)
DEFAULT_INCLUDE = [
    "exports/**/*.png",
    "exports/**/*.jpg",
    "runs/*.json",
    ".pytest_cache/**",
    ".ruff_cache/**",
]

# Patterns to never touch
DEFAULT_EXCLUDE = [
    "artifacts/**",
    ".git/**",
    "secrets/**",
    "secrets-local/**",
    "node_modules/**",
]


def should_exclude(path: Path) -> bool:
    """Check if path matches any exclude pattern."""
    for pattern in DEFAULT_EXCLUDE:
        if path.match(pattern):
            return True
    return False


def find_stale_files(days: int, include_patterns: list = None) -> list:
    """Find files matching patterns and older than `days` days."""
    if include_patterns is None:
        include_patterns = DEFAULT_INCLUDE

    cutoff_time = datetime.now() - timedelta(days=days)
    stale_files = []

    for pattern in include_patterns:
        for file_path in REPO_ROOT.glob(pattern):
            if file_path.is_file():
                mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                if mtime < cutoff_time and not should_exclude(file_path):
                    stale_files.append(file_path)
                    logger.info(f"Found stale: {file_path} (modified {mtime})")

    return stale_files


def archive_file(file_path: Path, manifest: dict) -> bool:
    """Move file to archive directory, creating necessary directories."""
    try:
        # Determine archive path: data/archives/YYYY/MM/
        now = datetime.now()
        archive_dir = ARCHIVE_BASE / str(now.year) / f"{now.month:02d}"
        archive_dir.mkdir(parents=True, exist_ok=True)

        # Preserve original relative path in archive filename
        rel_path = file_path.relative_to(REPO_ROOT)
        safe_name = str(rel_path).replace("/", "__")
        archived_path = archive_dir / safe_name

        # Move file
        shutil.move(str(file_path), str(archived_path))
        logger.info(f"Archived: {file_path} -> {archived_path}")

        # Record in manifest
        manifest["archived_files"].append(
            {
                "original_path": str(rel_path),
                "archive_path": str(archived_path.relative_to(REPO_ROOT)),
                "timestamp_utc": datetime.utcnow().isoformat() + "Z",
                "original_mtime": datetime.fromtimestamp(
                    file_path.stat().st_mtime
                ).isoformat(),
            }
        )

        return True
    except Exception as e:
        logger.error(f"Failed to archive {file_path}: {e}")
        return False


def save_manifest(manifest: dict):
    """Save undo manifest to data/archives/manifests/."""
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    manifest_path = MANIFEST_DIR / f"archive-run-{now.isoformat()}.json"

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    logger.info(f"Manifest saved: {manifest_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Archive stale workspace files to data/archives/"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=14,
        help="Archive files older than N days (default: 14)",
    )
    parser.add_argument(
        "--include",
        nargs="+",
        default=DEFAULT_INCLUDE,
        help="File patterns to consider (glob-style)",
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        default=DEFAULT_EXCLUDE,
        help="Patterns to never touch",
    )
    parser.add_argument(
        "--stage",
        action="store_true",
        help="Stage archived files in git (optional)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be archived without moving",
    )

    args = parser.parse_args()

    logger.info(f"Scanning for files older than {args.days} days...")
    stale_files = find_stale_files(args.days, args.include)

    if not stale_files:
        logger.info("No stale files found.")
        return 0

    logger.info(f"Found {len(stale_files)} stale file(s).")

    if args.dry_run:
        logger.info("[DRY RUN] Would archive:")
        for f in stale_files:
            logger.info(f"  - {f.relative_to(REPO_ROOT)}")
        return 0

    # Archive files
    manifest = {
        "archive_run_timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "archived_files": [],
    }

    for file_path in stale_files:
        archive_file(file_path, manifest)

    save_manifest(manifest)

    # Optional: stage in git
    if args.stage and manifest["archived_files"]:
        try:
            import subprocess

            subprocess.run(
                ["git", "add", str(ARCHIVE_BASE)],
                cwd=REPO_ROOT,
                check=True,
                capture_output=True,
            )
            logger.info("Staged archives/ in git.")
        except Exception as e:
            logger.warning(f"Could not stage in git: {e}")

    logger.info(f"Archived {len(manifest['archived_files'])} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

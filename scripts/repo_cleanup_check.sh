#!/usr/bin/env bash
# Quick repo inspection script (non-destructive)
# Prints disk usage, largest files, git status summary, and untracked files preview.

set -euo pipefail

here=$(pwd)
echo "Repository inspection at: $here"
echo

echo "1) Git status (short):"
git status --short || true
echo

echo "2) Untracked files (preview):"
git clean -nd || true
echo

echo "3) Ignored files (preview):"
git clean -ndX || true
echo

echo "4) Top owner-level disk usage (top 30):"
du -sh * 2>/dev/null | sort -h | tail -n 30 || true
echo

echo "5) Largest files under repo (top 30):"
find . -type f -printf "%s %p\n" 2>/dev/null | sort -n | tail -n 30 | awk '{printf "%10.2f MB %s\n", $1/1024/1024, $2}' || true
echo

echo "6) Untracked files list (first 200 lines):"
git ls-files --others --exclude-standard | sed -n '1,200p' || true
echo

echo "7) Suggested next commands (no automatic deletion):"
echo "  - Review the largest files above and decide which to archive or remove." 
echo "  - To preview removal: git clean -nd ; To apply: git clean -fd  # CAUTION"
echo "  - To preview ignored removal: git clean -ndX ; To apply: git clean -fdX  # CAUTION"
echo "  - To archive a directory: tar -czvf ../repo-archive-\$(date +%Y%m%d%H%M).tar.gz <path>"
echo

echo "Inspection complete. Reply here with which files/paths you'd like me to archive or remove, and I'll prepare the exact commands or create tarballs for you."


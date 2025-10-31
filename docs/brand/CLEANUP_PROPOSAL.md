# Repository cleanup proposal and safe checklist

This document describes a non-destructive plan to inspect and tidy the repository. It does NOT perform deletions automatically. Follow the listed commands locally and confirm before removing or archiving files.

## Goals

- Reduce clutter and large unused files in the repo root and workspace.
- Ensure secrets are not committed (verify `.env.local` is sanitized / gitignored).
- Add a reproducible, auditable checklist for maintainers to run before commit/push.

## Quick safety checklist (run locally)

1. Inspect git status and untracked files

```bash
git status --short
git clean -ndX    # list candidate ignored files that would be removed
git clean -nd     # list untracked files that would be removed
```

2. Find largest files and directories (interactive review)

```bash
# top-level disk usage (sorted, human readable)
du -sh * | sort -h | tail -n 30

# largest files anywhere in repo (top 30)
find . -type f -exec du -h {} + | sort -h | tail -n 30
```

3. Verify `.env.local` and secrets

```bash
# Check for .env.local in git history (requires git log access)
git ls-files --others --exclude-standard
grep -n "OPENAI\|GITHUB_TOKEN\|PASSWORD\|SECRET\|PRIVATE_KEY" -R --line-number --no-messages || true
```

If you see secrets, rotate them immediately and remove them from the repo with the recommended tools (git filter-repo or BFG) — ask me and I'll provide exact commands.

4. Archive large, infrequently used assets

If `data/digital_assets/` or `archives/` contain very large files, consider moving them to an `archives/` folder outside the repo (or to cloud storage) and replacing with small metadata pointers.

5. Add or update `.gitignore` for local build artifacts

Common entries to add if applicable:

```
# Python
.venv/
__pycache__/
*.py[cod]

# Node
node_modules/

# Local env
.env.local
.env.local.bak

# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.sublime-project
```

## Suggested non-destructive commands you can run now

List disk usage and candidate files to move:

```bash
# show the 50 largest files under repo
find . -type f -printf "%s %p\n" | sort -n | tail -n 50 | awk '{printf "%10.2f MB %s\n", $1/1024/1024, $2}'
```

Preview removal of untracked files (safe):

```bash
git clean -nd    # preview
# when ready: git clean -fd  # remove untracked files (CAUTION)
```

Preview removal of ignored files (safe):

```bash
git clean -ndX   # preview
# when ready: git clean -fdX  # remove ignored files (CAUTION)
```

## If you want me to help perform safe moves

Tell me exactly which files or directories you want archived or removed. I can:

- Create a tarball of selected paths and place it in `/home/tec_tgcr/archives/` (non-destructive).
- Add entries to `.gitignore` and commit them.
- Create a `scripts/` helper to automate archiving large assets.

## Next steps for maintainers

1. Run the inspection script (`scripts/repo_cleanup_check.sh`) added to the repo (see below) to get a pre-filled report.
2. Review the report and decide which files to archive or remove.
3. If you need help rewriting git history to remove past secrets, ask me and I will provide a safe plan using `git filter-repo`.

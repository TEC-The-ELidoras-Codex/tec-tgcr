# Cross‑device unity — same tools, same UX

Goal: you can open TEC:TGCR on any machine and get the same commands, tests, and editor behavior.

## What’s standardized

- VS Code workspace: `tec-tgcr.code-workspace`
- VS Code settings/tasks: `.vscode/{settings,launch,tasks,extensions}.json` (tracked)
- Python: `.venv` per-repo with pinned deps in `pyproject.toml`
- CLI entry: `tec-agent` (Typer) and `python -m tec_tgcr.cli`
- Tests: pytest via task “Python: Run pytest”

## One‑time bootstrap per machine (Windows)

Run the bootstrap script from the repo root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/bootstrap.ps1
```

What it does:

- Creates `.venv` and installs the package (editable)
- Installs pytest (dev extras optional)
- Verifies `tec-agent --help`
- Prints quick commands to run tests and pack support bundle

## Optional: Dev extras

If you need docs export features that depend on `python-docx` (may require build tools on some Python versions):

```powershell
.\.venv\Scripts\python.exe -m pip install -e .[dev]
```

## Keep in sync

- Commit `.vscode/*` and `tec-tgcr.code-workspace` so tasks/settings travel.
- Prefer `.env.example` with placeholders; never commit real secrets.
- Use `docs/WP-CONFIG-SNIPPETS.md` for production WordPress secrets (server-side only).

# Relocate repository off OneDrive

This guide and helper script will move a local clone of this repository out of OneDrive to a new local path while preserving Git history and verifying the codebase.

Why move?

- OneDrive can interfere with file locking and Git operations. Local developer clones outside OneDrive avoid accidental sync conflicts and improve build/tooling stability.

Quick plan

1. Choose a destination path on your machine, e.g. `C:\Projects\tec-tgcr`.
2. Run the helper script: `. emplates\move_repo_from_onedrive.ps1 -Destination 'C:\Projects\tec-tgcr'` (from the repository root).
3. Open the destination folder in VS Code and run the tests to validate.
4. Optional: Remove or archive the OneDrive copy after verifying the destination is healthy.

Notes & cautions

- The script uses `robocopy` when available for robust copying.
- If `.git` is not copied correctly the script will warn and attempt a best-effort copy.
- After moving, update any tools or shortcuts that point to the old OneDrive path.

Manual commands (safe, copy-first approach)

```powershell
# From the OneDrive repo root
$dest = 'C:\Projects\tec-tgcr'
New-Item -ItemType Directory -Path $dest -Force
robocopy . $dest /MIR /COPYALL /R:3 /W:5

# Verify
Set-Location $dest
git status
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .[dev]
python -m pytest -q
```

Afterwards

- Confirm the Git remote is unchanged and pushes/pulls work from the new location.
- If you open the project in VS Code, be sure to point the workspace to the destination path.

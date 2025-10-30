"""SharePoint publishing integration for TEC agents.

Dry-run by default. Produces Microsoft 365 CLI commands and can execute them
only when explicitly forced.
"""

from __future__ import annotations
from __future__ import annotations

import json
import shlex
import subprocess
from pathlib import Path
from typing import Iterable, List


class SharePointPublisherTool:
    """Wraps Microsoft 365 CLI commands for SharePoint file deployment."""

    name = "sharepoint_publish"
    description = "Publish static assets to SharePoint using the Microsoft 365 CLI."

    def __init__(
        self,
        site_url: str,
        target_folder: str,
        files: Iterable[Path],
        dry_run: bool = True,
    ) -> None:
        self.site_url = site_url
        self.target_folder = target_folder.strip("/")
        self.files = [Path(file) for file in files]
        self.dry_run = dry_run

    def _build_command(self, file_path: Path) -> List[str]:
        return [
            "m365",
            "spo",
            "file",
            "add",
            "--webUrl",
            self.site_url,
            "--folder",
            f"SiteAssets/{self.target_folder}",
            "--path",
            str(file_path),
            "--overwrite",
        ]

    def login_command(self) -> str:
        """Return the device code login command for convenience."""
        return "m365 login --authType deviceCode"

    def run(self, query: str) -> str:
        """Execute (or preview) SharePoint uploads based on configured files."""
        responses: List[str] = []
        execute = not self.dry_run and "force" in query.lower()

        for file_path in self.files:
            cmd = self._build_command(file_path)
            pretty = " ".join(shlex.quote(part) for part in cmd)
            if execute:
                try:
                    result = subprocess.run(
                        cmd, capture_output=True, text=True, check=True
                    )
                    summary = {
                        "file": str(file_path),
                        "status": "uploaded",
                        "stdout": result.stdout.strip(),
                    }
                except (
                    subprocess.CalledProcessError
                ) as exc:  # pragma: no cover - external call guard
                    summary = {
                        "file": str(file_path),
                        "status": "error",
                        "stderr": exc.stderr.strip() if exc.stderr else "",
                    }
                responses.append(json.dumps(summary, indent=2))
            else:
                responses.append(f"DRY RUN → {pretty}")

        if execute:
            responses.append("Execution complete. Remove 'force' to preview only.")
        else:
            responses.append("Preview mode. Append 'force' to execute uploads.")
        return "\n".join(responses)

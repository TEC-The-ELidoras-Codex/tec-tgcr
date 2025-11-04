"""
Data ingestion layer for LuminAI copilot.

Gathers context from GitHub (issues, PRs, commits), Project #6, and research corpus.
Generates compressed context file for ChatGPT/Copilot consumption.

Example:
    python -m tec_tgcr.data_ingestion fetch-context
    # Outputs: data/context-latest.json
"""

import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from pathlib import Path

import httpx
from pydantic import BaseModel, Field


class GitHubIssue(BaseModel):
    """GitHub issue summary."""
    number: int
    title: str
    labels: List[str]
    state: str
    assignee: Optional[str] = None
    milestone: Optional[str] = None
    created_at: str
    updated_at: str


class ProjectItem(BaseModel):
    """GitHub Project item summary."""
    title: str
    status: str  # Column name
    priority: Optional[str] = None
    owner: Optional[str] = None


class MotifEntry(BaseModel):
    """Music motif from research corpus."""
    name: str
    theme: str
    genre: Optional[str] = None
    resonance_index: float = Field(ge=0, le=10)


class CopilotContext(BaseModel):
    """Complete context snapshot for LuminAI copilot."""
    timestamp: datetime
    summary: str
    github: Dict[str, Any]
    project: Dict[str, Any]
    research: Dict[str, Any]
    team: Dict[str, Any]


class FoldContextIngestion:
    """Gathers all context for LuminAI copilot."""

    def __init__(self, github_token: Optional[str] = None):
        """Initialize with optional GitHub token."""
        self.github_token = github_token or os.getenv("GITHUB_TOKEN", "")
        self.repo_owner = "TEC-The-ELidoras-Codex"
        self.repo_name = "tec-tgcr"
        self.base_url = "https://api.github.com"
        self.client = httpx.Client(
            headers={"Authorization": f"token {self.github_token}"} if self.github_token else {},
            timeout=10.0,
        )

    def fetch_issues(self, state: str = "open", limit: int = 20) -> List[GitHubIssue]:
        """Fetch open issues from GitHub."""
        url = (
            f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/issues"
            f"?state={state}&per_page={limit}&sort=updated"
        )
        try:
            resp = self.client.get(url)
            resp.raise_for_status()
            return [
                GitHubIssue(
                    number=issue["number"],
                    title=issue["title"],
                    labels=[label["name"] for label in issue["labels"]],
                    state=issue["state"],
                    assignee=issue["assignee"]["login"] if issue["assignee"] else None,
                    milestone=issue["milestone"]["title"] if issue["milestone"] else None,
                    created_at=issue["created_at"],
                    updated_at=issue["updated_at"],
                )
                for issue in resp.json()
            ]
        except Exception as e:
            print(f"Error fetching issues: {e}")
            return []

    def fetch_pull_requests(self, state: str = "open", limit: int = 10) -> List[Dict[str, Any]]:
        """Fetch open PRs from GitHub."""
        url = (
            f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/pulls"
            f"?state={state}&per_page={limit}&sort=updated"
        )
        try:
            resp = self.client.get(url)
            resp.raise_for_status()
            return [
                {
                    "number": pr["number"],
                    "title": pr["title"],
                    "author": pr["user"]["login"],
                    "state": pr["state"],
                    "created_at": pr["created_at"],
                    "updated_at": pr["updated_at"],
                    "labels": [label["name"] for label in pr["labels"]],
                }
                for pr in resp.json()
            ]
        except Exception as e:
            print(f"Error fetching PRs: {e}")
            return []

    def fetch_recent_commits(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Fetch recent commits."""
        url = (
            f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/commits"
            f"?per_page={limit}"
        )
        try:
            resp = self.client.get(url)
            resp.raise_for_status()
            return [
                {
                    "sha": commit["sha"][:7],
                    "message": commit["commit"]["message"].split("\n")[0],
                    "author": commit["commit"]["author"]["name"],
                    "date": commit["commit"]["author"]["date"],
                }
                for commit in resp.json()
            ]
        except Exception as e:
            print(f"Error fetching commits: {e}")
            return []

    def load_research_corpus(self) -> Dict[str, Any]:
        """Load research corpus metadata."""
        research_root = Path(__file__).parent.parent.parent / "research"

        album_analysis_count = 0
        codex_motifs = []

        if (research_root / "ALBUM_ANALYSIS").exists():
            album_analysis_count = len(
                list((research_root / "ALBUM_ANALYSIS").glob("*.md"))
            )

        if (research_root / "CODEX").exists():
            codex_files = list((research_root / "CODEX").glob("*.md"))
            codex_motifs = [f.stem for f in codex_files][:5]  # Top 5 motifs

        return {
            "album_analysis_count": album_analysis_count,
            "codex_motif_count": len(codex_motifs),
            "recent_motifs": codex_motifs,
            "research_ready": album_analysis_count > 0 or len(codex_motifs) > 0,
        }

    def load_personas(self) -> Dict[str, str]:
        """Load team personas."""
        personas_root = Path(__file__).parent.parent.parent / "data" / "personas"

        personas = {}
        if personas_root.exists():
            for persona_file in personas_root.glob("*.md"):
                personas[persona_file.stem] = persona_file.stem.replace("-", " ").title()

        return personas or {
            "luminai": "Resonance Sentinel",
            "airth": "Verification Archaeologist",
            "arcadia": "Narrative Compressor",
            "ely": "Operations Technician",
            "kaznak": "Strategic Oscillator",
        }

    def analyze_commit_patterns(self) -> Dict[str, Any]:
        """Analyze recent commit patterns for team activity."""
        commits = self.fetch_recent_commits(limit=20)

        signals = {}
        for commit in commits:
            # Extract persona signal (fold:, airth:, ely:, etc.)
            msg = commit["message"]
            if ":" in msg:
                prefix = msg.split(":")[0].lower()
                if prefix in ["fold", "airth", "arcadia", "ely", "kaznak"]:
                    signals[prefix] = signals.get(prefix, 0) + 1

        return {
            "total_recent": len(commits),
            "persona_activity": signals,
            "latest_commits": [f"{c['sha']} {c['message']}" for c in commits[:3]],
        }

    def count_project_items(self) -> Dict[str, int]:
        """Count Project #6 items by status (requires more API access)."""
        # TODO: Implement via GraphQL ProjectV2 API
        # For now, return placeholder
        return {
            "backlog": 15,
            "ready": 8,
            "in_progress": 3,
            "blocked": 2,
            "done": 0,  # Running total not tracked here
        }

    def generate_summary(self, context: CopilotContext) -> str:
        """Generate human-readable summary of current state."""
        github_stats = context.github
        project_stats = context.project
        research_stats = context.research

        issues_p0 = len([i for i in github_stats.get("open_issues", []) if "P0" in i.get("labels", [])])
        blockers = project_stats.get("blocked_count", 0)
        active = project_stats.get("in_progress_count", 0)

        return (
            f"MVP: {project_stats.get('ready_count', 0)} ready, "
            f"{active} active, "
            f"{blockers} blocked | "
            f"P0 Issues: {issues_p0} | "
            f"Research: {research_stats.get('album_analysis_count', 0)} artists, "
            f"{research_stats.get('codex_motif_count', 0)} motifs"
        )

    def fetch_context(self) -> CopilotContext:
        """Fetch all context from GitHub, Project, and research corpus."""
        issues = self.fetch_issues(state="open")
        prs = self.fetch_pull_requests(state="open")
        commits = self.fetch_recent_commits()
        project_items = self.count_project_items()
        research = self.load_research_corpus()
        personas = self.load_personas()
        team_activity = self.analyze_commit_patterns()

        context = CopilotContext(
            timestamp=datetime.now(),
            summary="",  # Will be set below
            github={
                "open_issues": [issue.model_dump() for issue in issues],
                "open_prs": prs,
                "recent_commits": commits,
                "issue_count": len(issues),
                "pr_count": len(prs),
                "p0_issues": len([i for i in issues if "P0" in i.labels]),
                "p1_issues": len([i for i in issues if "P1" in i.labels]),
            },
            project=project_items,
            research=research,
            team={
                "personas": personas,
                "recent_activity": team_activity,
            },
        )

        context.summary = self.generate_summary(context)
        return context

    def save_context(self, context: CopilotContext, output_path: Optional[Path] = None) -> Path:
        """Save context to JSON file."""
        if output_path is None:
            output_path = (
                Path(__file__).parent.parent.parent / "data" / "context-latest.json"
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(context.model_dump(), f, indent=2, default=str)

        return output_path


def main():
    """CLI entry point."""
    import sys

    ingestion = FoldContextIngestion()

    if len(sys.argv) > 1 and sys.argv[1] == "fetch-context":
        context = ingestion.fetch_context()
        output = ingestion.save_context(context)
        print(f"✓ Context saved to {output}")
        print(f"Summary: {context.summary}")
    else:
        print("Usage: python -m tec_tgcr.data_ingestion fetch-context")


if __name__ == "__main__":
    main()

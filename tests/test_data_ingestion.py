"""
Unit tests for FOLD data ingestion module.

Tests GitHub API integration, research corpus loading, and context generation.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from tec_tgcr.data_ingestion import (
    CopilotContext,
    FoldContextIngestion,
    GitHubIssue,
    ProjectItem,
)


class TestGitHubIssue:
    """Test GitHub issue model."""

    def test_issue_creation(self):
        """Create a GitHub issue."""
        issue = GitHubIssue(
            number=42,
            title="Fix authentication bug",
            labels=["bug", "P0"],
            state="open",
            assignee="alice",
            milestone="v1.0",
            created_at="2025-01-01T00:00:00Z",
            updated_at="2025-01-02T00:00:00Z",
        )
        assert issue.number == 42
        assert issue.title == "Fix authentication bug"
        assert "P0" in issue.labels
        assert issue.state == "open"


class TestProjectItem:
    """Test Project item model."""

    def test_item_creation(self):
        """Create a project item."""
        item = ProjectItem(
            title="Implement motif search",
            status="In Progress",
            priority="P0",
            owner="bob",
        )
        assert item.title == "Implement motif search"
        assert item.status == "In Progress"


class TestFoldContextIngestion:
    """Test context ingestion."""

    def setup_method(self):
        """Set up test fixtures."""
        self.ingestion = FoldContextIngestion(github_token="test-token")

    @patch("httpx.Client.get")
    def test_fetch_issues_success(self, mock_get):
        """Test successful GitHub issue fetch."""
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "number": 1,
                "title": "Bug: empty issues",
                "labels": [{"name": "bug"}, {"name": "P1"}],
                "state": "open",
                "assignee": None,
                "milestone": None,
                "created_at": "2025-01-01T00:00:00Z",
                "updated_at": "2025-01-02T00:00:00Z",
            }
        ]
        mock_get.return_value = mock_response

        issues = self.ingestion.fetch_issues()

        assert len(issues) == 1
        assert issues[0].number == 1
        assert issues[0].title == "Bug: empty issues"
        assert "bug" in issues[0].labels

    @patch("httpx.Client.get")
    def test_fetch_issues_error(self, mock_get):
        """Test error handling during issue fetch."""
        mock_get.side_effect = Exception("Network error")

        issues = self.ingestion.fetch_issues()

        assert issues == []

    @patch("httpx.Client.get")
    def test_fetch_prs_success(self, mock_get):
        """Test successful PR fetch."""
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "number": 10,
                "title": "Add motif search",
                "user": {"login": "charlie"},
                "state": "open",
                "created_at": "2025-01-01T00:00:00Z",
                "updated_at": "2025-01-02T00:00:00Z",
                "labels": [{"name": "feature"}],
            }
        ]
        mock_get.return_value = mock_response

        prs = self.ingestion.fetch_pull_requests()

        assert len(prs) == 1
        assert prs[0]["number"] == 10
        assert prs[0]["author"] == "charlie"

    @patch("httpx.Client.get")
    def test_fetch_commits_success(self, mock_get):
        """Test successful commit fetch."""
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "sha": "abc1234567890",
                "commit": {
                    "message": "fold: add context ingestion\n\nMore details",
                    "author": {"name": "Alice", "date": "2025-01-01T00:00:00Z"},
                },
            }
        ]
        mock_get.return_value = mock_response

        commits = self.ingestion.fetch_recent_commits()

        assert len(commits) == 1
        assert commits[0]["sha"] == "abc1234"
        assert commits[0]["message"] == "fold: add context ingestion"

    def test_load_research_corpus(self):
        """Test research corpus loading."""
        research = self.ingestion.load_research_corpus()

        assert "album_analysis_count" in research
        assert "codex_motif_count" in research
        assert "research_ready" in research
        assert isinstance(research["album_analysis_count"], int)

    def test_load_personas(self):
        """Test persona loading."""
        personas = self.ingestion.load_personas()

        assert "luminai" in personas or len(personas) > 0
        assert isinstance(personas, dict)

    @patch.object(FoldContextIngestion, "fetch_issues")
    @patch.object(FoldContextIngestion, "fetch_pull_requests")
    @patch.object(FoldContextIngestion, "fetch_recent_commits")
    @patch.object(FoldContextIngestion, "count_project_items")
    def test_fetch_context(self, mock_project, mock_commits, mock_prs, mock_issues):
        """Test complete context fetch."""
        mock_issues.return_value = [
            GitHubIssue(
                number=1,
                title="Test issue",
                labels=["P0"],
                state="open",
                created_at="2025-01-01T00:00:00Z",
                updated_at="2025-01-02T00:00:00Z",
            )
        ]
        mock_prs.return_value = [
            {"number": 1, "title": "Test PR", "author": "alice", "state": "open"}
        ]
        mock_commits.return_value = [
            {"sha": "abc", "message": "fold: test", "author": "bob", "date": "2025-01-01"}
        ]
        mock_project.return_value = {
            "backlog": 5,
            "ready": 3,
            "in_progress": 1,
            "blocked": 0,
        }

        context = self.ingestion.fetch_context()

        assert isinstance(context, CopilotContext)
        assert context.github["issue_count"] == 1
        assert context.github["pr_count"] == 1
        assert context.github["p0_issues"] == 1
        assert context.summary is not None
        assert "ready" in context.project

    def test_save_context(self):
        """Test context file saving."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "context.json"

            context = CopilotContext(
                timestamp="2025-01-01T00:00:00Z",
                summary="Test summary",
                github={
                    "open_issues": [],
                    "open_prs": [],
                    "recent_commits": [],
                    "issue_count": 0,
                    "pr_count": 0,
                    "p0_issues": 0,
                    "p1_issues": 0,
                },
                project={"backlog": 0, "ready": 0},
                research={"album_analysis_count": 0, "codex_motif_count": 0},
                team={"personas": {}},
            )

            result_path = self.ingestion.save_context(context, output_path)

            assert result_path.exists()
            with open(result_path) as f:
                data = json.load(f)
            assert data["summary"] == "Test summary"
            assert data["github"]["issue_count"] == 0

    def test_analyze_commit_patterns(self):
        """Test commit pattern analysis."""
        with patch.object(self.ingestion, "fetch_recent_commits") as mock_fetch:
            mock_fetch.return_value = [
                {"sha": "abc", "message": "fold: add feature", "author": "alice", "date": "2025-01-01"},
                {"sha": "def", "message": "airth: verify", "author": "bob", "date": "2025-01-02"},
                {"sha": "ghi", "message": "ely: deploy", "author": "charlie", "date": "2025-01-03"},
            ]

            patterns = self.ingestion.analyze_commit_patterns()

            assert "persona_activity" in patterns
            assert patterns["total_recent"] == 3
            assert patterns["persona_activity"].get("fold", 0) > 0

    def test_generate_summary(self):
        """Test context summary generation."""
        context = CopilotContext(
            timestamp="2025-01-01T00:00:00Z",
            summary="",
            github={
                "open_issues": [
                    {"number": 1, "title": "Issue 1", "labels": ["P0"], "state": "open"}
                ],
                "open_prs": [{"number": 1, "title": "PR 1"}],
                "recent_commits": [],
                "issue_count": 1,
                "pr_count": 1,
                "p0_issues": 1,
                "p1_issues": 0,
            },
            project={"backlog": 10, "ready": 3, "in_progress": 2, "blocked": 1},
            research={"album_analysis_count": 2, "codex_motif_count": 5},
            team={"personas": {}},
        )

        summary = self.ingestion.generate_summary(context)

        assert "ready" in summary
        assert "active" in summary
        assert "blocked" in summary


class TestCopilotContext:
    """Test the CopilotContext model."""

    def test_context_creation(self):
        """Create a copilot context."""
        context = CopilotContext(
            timestamp="2025-01-01T00:00:00Z",
            summary="Test summary",
            github={"issue_count": 5},
            project={"ready": 3},
            research={"codex_motifs": 10},
            team={"personas": {"luminai": "Sentinel"}},
        )
        assert context.summary == "Test summary"
        assert context.github["issue_count"] == 5

    def test_context_serialization(self):
        """Serialize context to dict."""
        context = CopilotContext(
            timestamp="2025-01-01T00:00:00Z",
            summary="Test",
            github={},
            project={},
            research={},
            team={},
        )
        data = context.model_dump()
        assert isinstance(data, dict)
        assert "timestamp" in data
        assert "summary" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

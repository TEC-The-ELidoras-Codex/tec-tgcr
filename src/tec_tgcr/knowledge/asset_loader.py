"""Automatic knowledge asset loader — discovers and loads personas, guides, classification from source files.

This module provides a self-populating knowledge base. It automatically discovers all markdown files
in designated folders (personas, guides, classification, research) and exposes them as structured data.

No manual uploads needed. Changes to source files automatically reflect in the API.

Usage:
    loader = AssetLoader()
    personas = loader.load_personas()           # All 9 personas
    guides = loader.load_guides()               # All deployment/classification guides
    classification = loader.load_classification()  # Shareable/Internal rules
    system_info = loader.load_system_info()     # Integration guide, workflows
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional

from tec_tgcr.env import env_path


class AssetLoadError(Exception):
    """Raised when asset loading fails."""

    pass


class AssetLoader:
    """Automatically loads and caches knowledge assets from source files.

    Discovers and structures:
    - Personas (data/personas/*.md) → 9 structured persona specs
    - Guides (*.md files: PULL_AND_BUILD_GUIDE, GPT_*, etc.) → Deployment guides
    - Classification (SHAREABLE_VS_INTERNAL_CLASSIFICATION.md) → File classification rules
    - System Info (SYSTEM_INTEGRATION_GUIDE.md, etc.) → System architecture & workflows
    """

    def __init__(self, repo_root: Optional[Path] = None):
        """Initialize loader with repo root (defaults to workspace root)."""
        if repo_root is None:
            # Determine repo root relative to this file
            repo_root = Path(__file__).parents[3]

        self.repo_root = Path(repo_root) if not isinstance(repo_root, Path) else repo_root
        self.personas_dir = self.repo_root / "data" / "personas"
        self.guides_pattern = [
            self.repo_root / "PULL_AND_BUILD_GUIDE.md",
            self.repo_root / "SYSTEM_INTEGRATION_GUIDE.md",
            self.repo_root / "SHAREABLE_VS_INTERNAL_CLASSIFICATION.md",
            self.repo_root / "GPT_DEPLOYMENT_READY.md",
            self.repo_root / "GPT_PERSONAS_ATTACHMENT_DECISION.md",
            self.repo_root / "GPT_ATTACHMENT_CHEAT_SHEET.md",
        ]

    @staticmethod
    def _parse_markdown(path: Path) -> Dict[str, Any]:
        """Parse markdown file with optional YAML front matter.

        Returns dict with:
        - title: filename or markdown H1 title
        - content: markdown body
        - metadata: extracted YAML front matter (if present)
        """
        try:
            text = path.read_text(encoding="utf-8")

            # Simple YAML front matter parser (---...---)
            metadata = {}
            content = text

            if text.startswith("---"):
                # Extract YAML front matter
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    yaml_text = parts[1]
                    content = parts[2].strip()

                    # Simple YAML key: value parser
                    for line in yaml_text.split("\n"):
                        if ":" in line:
                            key, val = line.split(":", 1)
                            metadata[key.strip()] = val.strip()

            # Extract title from first H1 if not in metadata
            title = metadata.get("title", path.stem)
            if not title or title == path.stem:
                h1_match = re.search(r"^#\s+(.+?)$", content, re.MULTILINE)
                if h1_match:
                    title = h1_match.group(1).strip()

            return {
                "title": title,
                "content": content,
                "metadata": metadata,
                "path": str(path.relative_to(path.parent.parent.parent)),
            }
        except Exception as exc:
            raise AssetLoadError(f"Failed to parse {path}: {exc}") from exc

    @lru_cache(maxsize=1)
    def load_personas(self) -> Dict[str, Dict[str, Any]]:
        """Load all persona specs from data/personas/*.md.

        Returns:
            {
                "luminai": {"title": "...", "content": "...", "metadata": {...}, "path": "..."},
                "airth": {...},
                ...
            }

        Touches φᵗ (temporal availability) and Φᴱ (contextual potential via persona knowledge).
        """
        if not self.personas_dir.exists():
            return {}

        personas = {}
        for persona_file in sorted(self.personas_dir.glob("*.md")):
            name = persona_file.stem
            try:
                personas[name] = self._parse_markdown(persona_file)
            except AssetLoadError as e:
                personas[name] = {"error": str(e)}

        return personas

    @lru_cache(maxsize=1)
    def load_guides(self) -> Dict[str, Dict[str, Any]]:
        """Load all deployment and reference guides.

        Returns:
            {
                "pull_and_build": {"title": "...", "content": "...", ...},
                "gpt_deployment": {...},
                "system_integration": {...},
                ...
            }

        Touches ψʳ (structural cadence of deployment workflow) and Φᴱ (contextual enablement).
        """
        guides = {}
        for guide_path in self.guides_pattern:
            if guide_path.exists():
                key = guide_path.stem.lower().replace("-", "_")
                try:
                    guides[key] = self._parse_markdown(guide_path)
                except AssetLoadError as e:
                    guides[key] = {"error": str(e)}

        return guides

    @lru_cache(maxsize=1)
    def load_classification(self) -> Dict[str, Any]:
        """Load file classification rules (shareable vs. internal).

        Returns structured classification with categories:
        - shareable: SHAREABLE files & folders
        - internal: INTERNAL-ONLY files & folders
        - conditional: Files needing sanitization
        - prefixes: Naming conventions

        Touches ψʳ (structural integrity of repo) and Φᴱ (trust/security).
        """
        classification_file = (
            self.repo_root / "SHAREABLE_VS_INTERNAL_CLASSIFICATION.md"
        )
        if not classification_file.exists():
            return {"error": "Classification guide not found"}

        parsed = self._parse_markdown(classification_file)

        # Extract sections programmatically (basic parsing)
        content = parsed["content"]
        return {
            "title": parsed["title"],
            "content": content,
            "path": parsed["path"],
            "categories": self._extract_classification_sections(content),
        }

    @staticmethod
    def _extract_classification_sections(content: str) -> Dict[str, List[str]]:
        """Extract 🟢 SHAREABLE, 🔴 INTERNAL, 🟡 CONDITIONAL sections from markdown.

        Returns dict mapping category → list of items.
        """
        sections = {"shareable": [], "internal": [], "conditional": []}

        lines = content.split("\n")
        current_section = None

        for line in lines:
            if "🟢 SHAREABLE" in line or "SHAREABLE" in line:
                current_section = "shareable"
            elif "🔴 INTERNAL" in line or "INTERNAL" in line:
                current_section = "internal"
            elif "🟡 CONDITIONAL" in line or "CONDITIONAL" in line:
                current_section = "conditional"
            elif current_section and line.startswith(("- ", "* ")):
                # Extract bullet item
                item = line.lstrip("- *").strip()
                if item:
                    sections[current_section].append(item)

        return sections

    @lru_cache(maxsize=1)
    def load_system_info(self) -> Dict[str, Any]:
        """Load system integration guide and core infrastructure info.

        Returns system workflows, diagrams, next steps, verification checklist.

        Touches φᵗ (temporal flow of onboarding) and Φᴱ (system coherence).
        """
        system_file = self.repo_root / "SYSTEM_INTEGRATION_GUIDE.md"
        if not system_file.exists():
            return {"error": "System integration guide not found"}

        return self._parse_markdown(system_file)

    def load_all(self) -> Dict[str, Any]:
        """Load all knowledge assets at once.

        Returns unified knowledge base:
        {
            "personas": {...},
            "guides": {...},
            "classification": {...},
            "system": {...},
            "metadata": {
                "loaded_at": "...",
                "repo_root": "...",
                "persona_count": 9,
                "guide_count": 6,
            }
        }

        Touches all three TGCR variables: φᵗ (unified temporal availability),
        ψʳ (structural coherence of knowledge system), Φᴱ (full contextual potential).
        """
        import datetime

        personas = self.load_personas()
        guides = self.load_guides()
        classification = self.load_classification()
        system_info = self.load_system_info()

        return {
            "personas": personas,
            "guides": guides,
            "classification": classification,
            "system": system_info,
            "metadata": {
                "loaded_at": datetime.datetime.utcnow().isoformat(),
                "repo_root": str(self.repo_root),
                "persona_count": len(personas),
                "guide_count": len(guides),
                "status": "auto-synced",
            },
        }

    def to_json(self) -> str:
        """Serialize all knowledge as JSON (for API responses).

        Returns JSON-formatted knowledge base (pretty-printed).
        """
        return json.dumps(self.load_all(), indent=2, default=str)


# Singleton instance for module-level access
_default_loader: Optional[AssetLoader] = None


def get_loader(repo_root: Optional[Path] = None) -> AssetLoader:
    """Get or create the default asset loader instance."""
    global _default_loader
    if _default_loader is None:
        _default_loader = AssetLoader(repo_root)
    return _default_loader

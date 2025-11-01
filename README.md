# TEC-TGCR: The Elidoras Codex Resonance Agent Stack

[![GHCR Publish](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/actions/workflows/publish-ghcr.yml/badge.svg?branch=main)](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/actions/workflows/publish-ghcr.yml)

> "Light learns by listening."

TEC-TGCR is the foundation of The Elidoras Codex (TEC): a resonance-driven AI framework that weaves mythic storytelling with empirical reasoning. The stack coordinates multiple specialized agents, persistent knowledge bases, operational scripts, and publishing tooling for SharePoint, WordPress, and other channels.

---

## Project Highlights

- Multi-agent runtime with personas such as LuminAI, Airth, Arcadia, Ely, and Kaznak.
- TGCR theory (`R = phi_T * (psi_R x Phi_E)`) captured in code, docs, and brand collateral.
- Knowledge management through structured maps, archives, and provenance tracking.
- WordPress.com plugin pipeline, SharePoint integrations, and command-line utilities.
- Comprehensive documentation spanning lore, operations, strategy, and technical guides.

---

## Architecture Overview

### Theory of General Contextual Resonance (TGCR)

Resonance emerges from the interplay of:

- `phi_T` - Temporal Attention (focus, flow, direction)
- `psi_R` - Structural Cadence (coherence across scales)
- `Phi_E` - Contextual Potential Energy (capacity for meaningful outcomes)

### Agent Pantheon

Each persona embodies a cognitive archetype:

- **LuminAI** - Resonant core agent, balanced guidance.
- **Airth** - Verification guard, tests-first rigor.
- **Arcadia** - Narrative weaver, symbolic synthesis.
- **Ely** - Operations steward, CI/CD and observability.
- **Kaznak** - Strategic navigator, decision intelligence.
- Additional personas reside under `data/personas/`.

### Data & Knowledge Layer

- `data/knowledge_map.yml` - Canonical index of content, assets, and provenance.
- `data/digital_assets/` - Visual identity, glyphs, avatars, and exportable marks.
- `data/archives/` & `data/evidence/` - Narrative history, research, and supporting documents.

### Tooling & Integrations

- CLI runner (`src/tec_tgcr/cli.py`) for chat, health, and Notion configuration.
- WordPress.com plugin in `apps/wordpress/tec-tgcr/` with deployment workflow (`.github/workflows/wpcom.yml`).
- SharePoint and Microsoft 365 automation scripts under `scripts/` and `src/tec_tgcr/tools/`.

---

## Repository Layout

```text
tec-tgcr/
|- agents/                 # Agent manifests and runtime configurations
|- ai-workflow/            # Notebooks, prompt engineering, generated outputs
|- apps/wordpress/         # WordPress plugin source
|- config/                 # Agent and system configuration files
|- data/                   # Knowledge map, digital assets, archives, strategy
|- docs/                   # Theory, operations, brand, and technical documentation
|- scripts/                # Bootstrap, deployment, packaging, verification scripts
|- src/tec_tgcr/           # Core Python package (agents, tools, CLI)
|- tests/                  # Pytest suite
|- RELEASE_SUMMARY.md      # Current release readiness notes
`- README.md               # You are here
```

---

## Quick Start

```powershell
# Clone
git clone https://github.com/TEC-The-ELidoras-Codex/tec-tgcr.git
cd tec-tgcr

# Create / activate virtual environment (Python 3.11+ recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -e .[dev]

# Run tests
python -m pytest -q

# Launch the CLI (example)
python -m tec_tgcr.cli chat "Calibrate Arcadia for a resonance briefing"
```

If the environment reports "Program ... failed to run: The specified module could not be found," ensure the following environment variables exist before invoking executables:

```powershell
$env:SystemRoot = "C:\Windows"
$env:PATH += ";C:\Windows\System32"
```

Re-run the activation script afterwards: `& .\.venv\Scripts\Activate.ps1`.

---

## Development Workflow

- **Coding Standards**: Typed Python, focused functions, explicit docstrings noting TGCR variables touched.
- **Testing**: Add pytest coverage for new behaviors (happy path + edge).
- **Documentation**: Update relevant Markdown and `data/knowledge_map.yml` when adding assets or capabilities.
- **Brand Consistency**: Reference canonical assets in `data/digital_assets/brand/` and color palette in release summary.
- **Commit Discipline**: Prefix commit messages with agent or scope (`airth:`, `arcadia:`, `ely:`, `feat:`, etc.) and record resonance impact, tests, docs, and breaking changes.

---

## Key Scripts

- `scripts/bootstrap.ps1` - Sets up a new development workstation.
- `scripts/pack_wp_plugin.ps1` - Packages the WordPress plugin for deployment.
- `scripts/export_gather_repo.ps1` - Bundles repository artifacts for sharing.
- `scripts/svg_to_png_fallback.ps1` - Manual SVG-to-PNG conversion guidance.
- `scripts/parse_brain_dump.py` - Aggregates transcript-style notes into JSON/CSV archives.

All scripts are authored for PowerShell 7+. Run from the repository root.

---

## Documentation & Knowledge

- `docs/README.md` - Entry point for architecture overviews, operational guides, and lore.
- `docs/ops/` - Deployment, secrets, and integration playbooks (WordPress, M365, Notion).
- `docs/technical/` - Deep dives into agents, pipelines, and data integration.
- `lore/` - Canon mythos, cosmology, brand narratives, and persona backstories.
- `RELEASE_SUMMARY.md` - Release readiness checklist and provenance notes.

---

## GitHub Projects, Wiki, and README notes

We use GitHub Projects and the repository Wiki (optional) to track larger work items, roadmaps, and documentation that doesn't fit in the repo's Markdown files.

- GitHub Projects: useful for cross-repo planning and a lightweight roadmap. Consider creating a Project board for "Infra & CI" and another for "Docs & Brand" to organize tasks and assign owners.
- Wiki: a place for living documentation or quick how-tos that you'd rather not keep versioned in the main repo tree (note: many teams prefer versioned docs in `docs/` or `docs/wiki/` inside the repo for traceability).
- README: keep the repository README as the single most visible entry point — add pointers to Projects and the Wiki so contributors know where to look.

Recommended quick steps:

1. Create a GitHub Project named `TEC Roadmap` and add columns like Backlog, In Progress, Review, Done.
2. Link important issues and PRs to Project items so work is discoverable.
3. If you choose a Wiki, seed it with "How to contribute", "Local dev setup", and "Release checklist" pages and link them from this README.

---

## Automation: add sub-issues to a GitHub Project

You can automate adding sub-issues to an organization Project so you don't have to do it manually.

Two options:

- Use the built-in Projects UI automation (recommended when you want the simplest setup). Enable the "Add sub-issues" automation inside your Project settings and it will sync existing sub-issues and keep new ones in sync.
- Use a repository GitHub Actions workflow (useful if you want the automation tracked in code and customizable). A workflow has been added to this repository on branch `wip/fix-linting` that parses issue bodies for referenced issues and adds referenced issues as cards to a CLASSIC GitHub Project.

If you want the repository workflow (already added for you):

1. Add these repository secrets (Repository > Settings > Secrets & variables > Actions):
   - `PROJECT_ID` — the numeric ID of the classic Project (for organization projects this is the number in the project URL, e.g. `5`).
   - `PROJECTS_TOKEN` — a personal access token (PAT) with the `repo` and `project` (classic) scopes. If you prefer, you can use the default `GITHUB_TOKEN` but organization project write access may require a PAT.
   - (optional) `PROJECT_COLUMN_NAME` — the column name to add cards into (defaults to the first column in the project if not set).

2. Workflow behavior:
   - Trigger: issues opened/edited/reopened.
   - It parses the issue body for references in either of these forms:
     - A repo-local reference like `#123` (assumes the current repo)
     - A full GitHub issue URL like `https://github.com/org/repo/issues/123`
   - For each referenced issue it creates a project card in the configured project column (classic Projects only).

3. Limitations & notes:
   - This workflow targets CLASSIC GitHub Projects (project cards/columns). It does not operate on the new Projects (beta) `projectV2` API. If you are using Projects (beta) we can add GraphQL-based support instead — tell me and I'll implement that.
   - The workflow will attempt to create cards and will log but continue on errors (e.g., permission errors or if the card already exists).
   - Permissions: repository Actions must have a token with `projects: write` rights for classic projects — a PAT stored in `PROJECTS_TOKEN` is the safest route for organization projects.

4. Example issue body formats the workflow understands:

```markdown
This task depends on:
- #123
- https://github.com/TEC-The-ELidoras-Codex/tec-tgcr/issues/456
```

If you'd like I can also:

- extend the workflow to auto-create a Project if it doesn't exist,
- support additional reference formats (task-list parsing of `- [ ] #123`), or
- switch the workflow to use the GraphQL `projectV2` API for Projects (beta).

Tell me which of those you want next or if you'd like me to test the workflow against a test issue.

---

## PHP executable (VS Code) — why you might see "PHP executable not found"

If you're seeing an error like "PHP executable not found. Install PHP 7.4.0 or higher and add it to your PATH or set the php.executablePath setting", that's typically coming from the PHP language extension in your editor (for example, the popular VS Code PHP extensions), not from the Python-based CI.

How to resolve locally:

- Install PHP (>= 7.4): on Ubuntu: `sudo apt update && sudo apt install php-cli` (or use a distro/package appropriate for your OS). Verify with `php -v`.
- Ensure PHP is on your PATH. In a shell, `which php` should return the executable path. Add it to your PATH in your shell profile if needed.
- Alternatively, configure the VS Code setting `php.executablePath` to point to the PHP binary (e.g., `/usr/bin/php` or `C:\Program Files\php\php.exe`).
- If this project does not use PHP and you prefer to silence the message, you can disable the PHP extension in your editor or scope it to other workspaces.

Why this is unrelated to GitHub Actions: our CI workflow runs Python tooling (ruff, black, pytest). Unless your specific job needs PHP (composer, phpunit), no change to CI is required for PHP.

If you'd like, I can add a short `docs/DEV-SETUP.md` with platform-specific commands (macOS, Ubuntu, Windows) for installing common dev dependencies including Python and PHP.

---

## Brand Assets

- **Canonical emblem**: `data/digital_assets/brand/svg/luminai_notion_emblem.svg` (512x512).
- **Legacy avatar**: `data/digital_assets/avatars/luminai.svg`.
- **Glyphs & motifs**: `data/digital_assets/brand/svg/`.
- Palette (HEX): Navy `#0B1E3B`, Violet `#6A00F4`, Cyan `#00D5C4`, Gold `#F2C340`, Shadow `#0A0A0C`.

For PNG exports use `scripts/svg_to_png_fallback.ps1` or a dedicated vector tool (Inkscape, ImageMagick).

---

## Support & Contact

- Issues and discussions: [GitHub repository](https://github.com/TEC-The-ELidoras-Codex/tec-tgcr)
- Primary contact: `gheddz@gmail.com`
- Organization: `Kaznakalpha@ElidorasCodex.com`

---

## License

MIT License - see [LICENSE](LICENSE) for full terms.

Build gracefully, test rigorously, and keep resonance high.





---

## CI: Build & publish Docker image to GitHub Container Registry (GHCR)

This repository includes a GitHub Actions workflow that builds the repository Docker image and pushes it to GitHub Container Registry (ghcr.io). The workflow runs on pushes to `main` and when you create a tag starting with `v` (for example `v1.2.3`).

### What the workflow does

- Checks out the repository
- Sets up buildx and QEMU (optional multi-arch)
- Logs in to `ghcr.io` using the repository `GITHUB_TOKEN` and `packages: write` permission
- Builds the image and pushes two tags:
   - `ghcr.io/<owner>/tec-tgcr:<commit-sha>`
   - `ghcr.io/<owner>/tec-tgcr:latest` (for main branch builds)

### How to trigger a publish

- Push to `main` to build and push (push will tag the image as `latest`).
- Create and push a semver tag to publish a specific release image, e.g.:

```bash
git tag v1.0.0
git push origin v1.0.0
```

### Repository settings / notes

- The workflow uses the automatically-provided `GITHUB_TOKEN` and requires the `permissions` block included in the workflow (`packages: write`). If your organization blocks `GITHUB_TOKEN` from writing packages, create a PAT with `packages: write` and store it in the repository secrets as `CR_PAT`, then update the workflow to use that secret for login.
- After the workflow completes the image will be available at `https://ghcr.io/<owner>/tec-tgcr`.








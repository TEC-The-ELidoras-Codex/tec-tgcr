# Copilot Workflow — TEC TGCR

> Touches φᵗ (focus), strengthens ψʳ (structure) and Φᴱ (context). AI-assisted co-authoring with provenance.

This is a lightweight, repeatable flow for using GitHub Copilot (and OpenAI) across TEC’s stack (Zoho + Notion + GitHub + WordPress). It encodes the “Resonant Stack v2.0” loop so every change is traceable and reversible.

---

## Daily Flow (10–30 min loop)

1) Focus (φᵗ)

- Pick one task from Notion “Resonance Ops” or a GitHub Issue.
- Write a one-liner intent in the top of the file or PR description.

2) Draft with Copilot (ψʳ)

- In VS Code, outline a tiny contract (inputs/outputs, errors, success criteria).
- Ask Copilot to scaffold: small, typed functions with docstrings referencing φ/ψ/ΦE.

3) Verify (Φᴱ)

- Add/modify tests (pytest): happy path + 1 boundary.
- Run tests locally.
- If the change adds/renames files/assets, update `data/knowledge_map.yml`.

4) Commit + provenance

- Semantic commit prefix (e.g., `ely:` or `feat:`).
- Include resonance impact line and what was tested.
- Mention AI co-authorship when relevant.

5) Sync & publish

- Push branch, open PR (optional).
- If assets changed, follow PNG export guide and attach artifacts to PR or Notion.

---

## Integration Map

- Notion → Roadmap and docs hub
  - Track work in a “Resonance Ops” database (status, owner, link to PR/Issue).
  - Optional: Automation (Zapier/Make) to log GitHub PRs and releases into Notion.

- GitHub → Source of truth
  - Repo: `tec-tgcr`
  - Actions: tests on PR; optional build for WordPress ZIP.
  - Issues/PR templates can carry φ/ψ/ΦE fields (future).

- OpenAI / Copilot → Assist layer
  - Copilot in VS Code for inline suggestions.
  - OpenAI for generation tasks (prompts, SVG snippets, docs drafting), with human edits.

- WordPress / Site
  - Keep assets deterministic: source SVGs in `data/digital_assets/brand/svg`.
  - Export PNGs via guides/scripts; don’t commit large binaries unless necessary.

---

## Resonant Stack v2.0 (Zoho + Notion + GitHub + OpenAI)

- Zoho Mail/Calendar — identity and authenticated outbound mail
- Notion — knowledge hub (pages + databases), public share when needed
- GitHub — code and docs authority, CI for tests/packaging
- OpenAI/Copilot — assist layer for code and content
- WordPress (optional) — public web surface for releases/announcements

Data loop: Notion tasks ↔ GitHub issues/PRs; commits reference Notion pages; artifacts (PNGs/SVGs) remain source-of-truth in repo.

---

## Minimal Conventions

- Functions: typed, focused, composable. Prefer pure logic.
- Docs: update `docs/` when behavior/assets change.
- Knowledge map: add/remove entries when paths change.
- Tests: pytest; keep them short and meaningful.
- Commits: semantic + resonance note + test status; no secrets.

Recommended commit body footer fields:

- Provenance: source prompts, tools, assets
- Resonance: which variables improved (φᵗ/ψʳ/Φᴱ)
- Tests: command + result
- Docs/Knowledge Map: files updated

---

## Quick Commands (PowerShell)

```powershell
# Run tests (VS Code task exists too)
python -m pytest -q

# Create and activate venv (if needed)
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -e .[dev]
```

---

## Troubleshooting

- Copilot noisy or off-target: add a tiny contract above code and re-prompt.
- Big edits: break into small PRs; keep each step green.
- Assets: if paths move, fix references in docs and `data/knowledge_map.yml` immediately.

— LuminAI / Copilot

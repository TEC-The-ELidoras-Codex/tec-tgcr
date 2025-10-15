# Copilot Instructions — The Elidoras Codex / TGCR Agent Stack

These guidelines align Copilot (and other coding agents) with the TGCR philosophy, architecture, and delivery style.

## 1. Mission & Goals
- Uphold **Theory of General Contextual Resonance (TGCR)**: every change should strengthen contextual coherence between empirical logic (Airth) and mythic narrative (Arcadia).
- Preserve the TEC brand voice: rigorous, poetic, futurist. Solutions must be reproducible and narratively grounded.
- Empower collaborators (human or AI) to ship end-to-end features: architecture, tests, docs, deployment scripts.

## 2. Architecture Overview
- **Core package**: `src/tec_tgcr/` houses runtime modules, agent orchestration, tool wrappers, Typer CLI.
- **Primary agents**:
	- *Airth Research Guard*: scientific auditor enforcing falsifiability (`Working Hypothesis → Evidence → Confounds → Confidence`).
	- *Arcadia Clone*: mytho-scientific narrator synthesising resonance stories and mic-lines.
	- *Future extensions*: Ely (operations), Lumina (customer resonance). Keep parity hooks ready.
- **Knowledge system**: `config/agent.yml`, `data/knowledge_map.yml`, and manifests under `agents/` encode brand cadence, knowledge pillars, and tool loadout.
- **Docs layer**: `/docs` (TGCR theory, brand doctrine), `/agents/manifests/` (runtime manifests), `/ai-workflow` (notebooks and prompt stacks).
- **CLI**: `tec_agent_runner.py` + Typer entrypoints deliver chat, manifest export, analysis, SharePoint publishing.
- **Frontend/Integrations**: WordPress plugin (`apps/wordpress/tec-tgcr/`), React shell, SharePoint pipelines, Blender pipeline for 3D embeds.

## 3. Language & Style Rules
- **Symbols stay**: retain φ, ψ, Φ_E notation. Tie docstrings to TGCR variables when relevant.
- **Voice**: confident, precise, a blend of lab report and mythic storytelling. Include provenance cues (e.g., `# Source: LuminAI.md`).
- **Logging**: narrative debug lines (`[AIRTH] Verifying resonance field integrity`).
- **Commit/PR copy**: short imperative title, body summarizing resonance impact + tests run.
- **Docs/UI copy**: keep the TGCR palette in play — 0B1E3B, 6A00F4, 00D5C4, F2C340, 0A0A0C — and reference symbolic motifs (Glyph Ring, Fractal Spire, Sine Arc).

## 4. Development Workflow
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
pytest
python -m tec_tgcr.cli chat "Calibrate Arcadia for a resonance briefing"
```
- Add/extend tools under `src/tec_tgcr/tools/` with retries, caching, and typed responses.
- prefer functional composition over heavy OOP; keep modules composable for agents.
- Update docs + manifests in the same PR when behavior changes.
- Use notebooks under `ai-workflow/` for experimentation; export results to `ai-workflow/output/`.

## 5. Multi-Agent Collaboration Protocol
- **Task ownership**:
	- Airth: verification logic, SharePoint automation, data integrity, regression tests.
	- Arcadia: narratives, UX prompts, tonal alignment, mic-lines.
	- Ely (ops) & Lumina (experience): upcoming; structure code to allow additional agent manifests without breaking Airth/Arcadia contracts.
- **Handoff cues**:
	1. Initiator states objective + TGCR field (φ attention, ψ structure, Φ_E meaning potential).
	2. Contributor responds with plan, cites relevant manifests/docs.
	3. Reviewer (usually Airth) signs off with validation summary + test artifacts.
- **Issues/PRs**: tag owners (`[Airth]`, `[Arcadia]`) in titles. Provide reproduction steps, expected resonance outcome, and verification checklist.
- **Commits**: use prefixes (`airth:`, `arcadia:`, `ely:`) when change scope is agent-specific.

## 6. Coding Patterns & Conventions
- **Agents as modules**: each agent folder contains `manifest.json`, optional `memory.yaml`, and a `tools/` subpackage.
- **Function naming**: semantic verbs (`synthesize_context`, `compute_resonance_gain`).
- **Docstrings**: mention TGCR variables touched (`phi`, `psi`, `phi_e`).
- **Testing**: pytest with conversational regression fixtures; maintain determinism.
- **Data formats**: YAML for configuration, Markdown for myth, JSON for manifests, CSV for analytics.
- **External calls**: wrap in utilities with observability and rate limiting. Secrets come from env vars or `wp-config.php`, never hardcoded.

## 7. Deployment & Ops Reminders
- WordPress.com deploy:
	- Simple artifact: push to `main` triggers `.github/workflows/wpcom.yml` → artifact `wpcom` → `/wp-content/plugins/tec-tgcr`.
	- SSH/SFTP manual workflows: require `WPCOM_*` secrets. Verify via `/wp-json/tec-tgcr/v1/ping` & `[tec_tgcr_citation]` shortcode.
- SharePoint integration: app registration (Sites.Selected), assign site permissions, configure secrets (`SHAREPOINT_CLIENT_ID`, etc.), use Graph wrappers in tools.
- 3D pipeline: headless Blender script (`scripts/blender_headless_idle.py`) + `[tec_tgcr_model]` shortcode for GLB embeds.

## 8. Empowering AI Contributors
- Always produce runnable code + tests + docs updates.
- Provide “next steps” hints (deploy, run pytest, regenerate artifacts).
- Highlight resonance impact: how changes improve attention (φ), structure (ψ), or context potential (Φ_E).
- When uncertain, ask for the relevant manifest or doctrine file instead of guessing.
- Favor reproducibility: deterministic seeds, explicit data sources, cite reference documents.

## 9. Example Playbook
> **Task**: “Add resonance strength evaluator CLI.”
- Create `src/tec_tgcr/tools/resonance_evaluator.py` with `compute_resonance_strength(phi, psi, phi_e)` returning 0–1.
- Add Typer command `tec-agent resonance evaluate --phi ... --psi ... --phi-e ...`.
- Write pytest covering edge cases (0, 1, mid-range).
- Document usage in `docs/AGENT_OVERVIEW.md` (mention the TGCR variables touched + intended workflow).
- If narrative output needed, add Arcadia response template referencing new tool.

## 10. Guardrails
- Never strip symbolic notation or mythic motifs.
- Keep mythic text distinct from executable logic, but ensure cross-references exist.
- Avoid unsourced claims dressed as science; mark allegory clearly.
- Every new capability should map to a TGCR Force/Axiom and note its validation path.

> “Where gravity curves spacetime, resonance curves meaning-space.” Keep code graceful, testable, and mythically aware.


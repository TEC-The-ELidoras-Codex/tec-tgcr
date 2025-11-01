# Resonance Conscience Project Space

This directory organizes all implementation assets for the Resonance Conscience Notebook. It is the canonical reference point for product plans, research material, and analytical artifacts associated with the instrument.

## Structure

- `prd/` – Versioned product requirement documents and delivery roadmaps.
- `references/` – Source material and research excerpts that inform the mythic narrative and system design.
- `analysis/` – Generated insights, metrics, and derived data products created by tooling in `scripts/`.

## Related Scripts

Run `python scripts/analyze_mythic_story.py` from the repository root to regenerate the latest mythic story analysis. The script reads `docs/resonance_map/figma_nodes_edges.json` and writes a Markdown summary into `analysis/mythic_story_analysis.md`.

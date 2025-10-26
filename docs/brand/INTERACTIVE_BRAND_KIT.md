65+-

# Interactive TEC Brand Kit

This document is a lightweight interactive guide for designers and automation agents. It points to the canonical, machine-readable `BRAND_MANIFEST.yml` and explains how to use it for design systems and Copilot/Spark prompts.

## Location

Canonical manifest: `data/digital_assets/brand/BRAND_MANIFEST.yml`

## Purpose

- Provide a single source of truth for colors, motifs, typography, and prompts.
- Enable automated tools (Copilot, Spark, Notion import scripts) to consume tokens and generate assets.

## Quick usage

1. Read `BRAND_MANIFEST.yml` to extract palette and typography.
2. Use `prompts.spark_landing_generator` when generating landing layouts or hero art.
3. For PNG exports, follow `docs/brand/PNG_EXPORT_GUIDE.md`.

## Designer notes

- Keep face and eyes unobscured.
- Follow the color ratio guidance in the manifest.
- Export SVG sources from `data/digital_assets/brand/svg/` and run `scripts/export_marketplace_header.ps1` to create web-ready PNGs.

## Automation hints

- When syncing to Notion or design systems, import the `palette` entries as tokens.
- Store provenance: include `provenance` block (author + date + source_docs) in all generated assets metadata.

---

Last updated: 2025-10-26

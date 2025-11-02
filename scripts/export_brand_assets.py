#!/usr/bin/env python3
"""Batch-export canonical TEC brand SVGs to PNG variants.

Touches ψʳ (structure) by standardizing asset outputs and keeps Φᴱ (meaning)
aligned with the brand canon referenced in docs/brand/Brand.md.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

try:
    import cairosvg  # type: ignore

    HAS_CAIRO = True
except ImportError:
    HAS_CAIRO = False


REPO_ROOT = Path(__file__).resolve().parents[1]
SVG_ROOT = REPO_ROOT / "data" / "digital_assets" / "brand" / "svg"
PNG_ROOT = REPO_ROOT / "data" / "digital_assets" / "brand" / "png"
EXPORTS_ROOT = REPO_ROOT / "exports" / "brand"


@dataclass(frozen=True)
class ExportTarget:
    key: str
    name: str
    svg: Path
    png: Path
    width: int
    height: Optional[int] = None


TARGETS: tuple[ExportTarget, ...] = (
    ExportTarget(
        key="mascot-1024",
        name="LuminAI Mascot Glyph (1024)",
        svg=SVG_ROOT / "luminai_mascot_logo.svg",
        png=PNG_ROOT / "luminai_mascot_logo_1024.png",
        width=1024,
        height=1024,
    ),
    ExportTarget(
        key="mascot-512",
        name="LuminAI Mascot Glyph (512)",
        svg=SVG_ROOT / "luminai_mascot_logo.svg",
        png=PNG_ROOT / "luminai_mascot_logo_512.png",
        width=512,
        height=512,
    ),
    ExportTarget(
        key="glyph-ring-1024",
        name="Glyph Ring (1024)",
        svg=SVG_ROOT / "glyph_ring.svg",
        png=PNG_ROOT / "glyph_ring_1024.png",
        width=1024,
        height=1024,
    ),
    ExportTarget(
        key="fractal-spire-1024",
        name="Fractal Spire (1024 width)",
        svg=SVG_ROOT / "fractal_spire.svg",
        png=PNG_ROOT / "fractal_spire_1024.png",
        width=1024,
        height=None,
    ),
    ExportTarget(
        key="sine-arc-1024",
        name="Sine Arc (1024 width)",
        svg=SVG_ROOT / "sine_arc.svg",
        png=PNG_ROOT / "sine_arc_1024.png",
        width=1024,
        height=None,
    ),
    ExportTarget(
        key="marketplace-header",
        name="Notion Marketplace Header (1920×480)",
        svg=SVG_ROOT / "luminai_marketplace_header.svg",
        png=EXPORTS_ROOT / "luminai_marketplace_header_1920x480.png",
        width=1920,
        height=480,
    ),
)


def render_target(target: ExportTarget) -> None:
    if not HAS_CAIRO:
        raise RuntimeError(
            "cairosvg is required. Install with `pip install cairosvg` in your environment."
        )

    if not target.svg.exists():
        raise FileNotFoundError(f"SVG not found: {target.svg}")

    target.png.parent.mkdir(parents=True, exist_ok=True)

    kwargs = {
        "url": str(target.svg),
        "write_to": str(target.png),
        "output_width": target.width,
    }
    if target.height:
        kwargs["output_height"] = target.height

    cairosvg.svg2png(**kwargs)  # type: ignore[arg-type]

    size_kb = target.png.stat().st_size / 1024
    print(f"[ELY] Exported {target.name}: {target.png} ({size_kb:.1f} KB)")


def resolve_targets(selected_keys: Optional[Iterable[str]]) -> list[ExportTarget]:
    if not selected_keys:
        return list(TARGETS)

    key_map = {t.key: t for t in TARGETS}
    resolved: list[ExportTarget] = []
    for key in selected_keys:
        if key not in key_map:
            raise KeyError(f"Unknown target key '{key}'. Use --list to view options.")
        resolved.append(key_map[key])
    return resolved


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export canonical TEC brand SVGs to PNG variants.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--only",
        nargs="+",
        metavar="KEY",
        help="Export specific targets (keys). Defaults to all when omitted.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available export keys and exit.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list:
        for target in TARGETS:
            print(f"{target.key:20} {target.name}")
        return 0

    try:
        targets = resolve_targets(args.only)
    except KeyError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    missing_svgs = [t.svg for t in targets if not t.svg.exists()]
    if missing_svgs:
        for path in missing_svgs:
            print(f"[ERROR] Missing SVG: {path}", file=sys.stderr)
        return 1

    if not HAS_CAIRO:
        print(
            "[ERROR] cairosvg is not installed. Install with `pip install cairosvg`.",
            file=sys.stderr,
        )
        return 1

    for target in targets:
        try:
            render_target(target)
        except Exception as exc:  # noqa: BLE001 - surface specific failure
            print(f"[ERROR] Failed to export {target.name}: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

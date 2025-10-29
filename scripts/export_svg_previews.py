"""
Small script to render SVG variants to PNG previews at multiple sizes.
Tries CairoSVG first, falls back to Inkscape CLI if available.
Outputs to data/digital_assets/brand/preview/{variant}/{size}.png
"""
from pathlib import Path
import shutil
import subprocess
import sys
import os
import argparse
from typing import Optional

VARIANTS_DIR = Path(__file__).resolve().parents[1] / 'data' / 'digital_assets' / 'brand' / 'svg'
OUT_DIR = Path(__file__).resolve().parents[1] / 'data' / 'digital_assets' / 'brand' / 'preview'
SIZES = [1024, 512, 256, 120]
VARIANTS = ['luminai_mascot_logo', 'luminai_mascot_logo_tight', 'luminai_mascot_logo_inset']


def render_with_cairosvg(src: Path, dst: Path, size: int) -> bool:
    try:
        import cairosvg
    except Exception:
        return False
    try:
        cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=size, output_height=size)
        return True
    except Exception as e:
        print(f"CairoSVG render failed for {src}: {e}")
        return False


def render_with_inkscape(src: Path, dst: Path, size: int, inkscape_cmd: Optional[str] = None) -> bool:
    """Render using Inkscape CLI.

    inkscape_cmd resolution order:
    1. explicit parameter
    2. INKSCAPE_PATH env var
    3. lookup on PATH
    """
    inkscape = inkscape_cmd or os.environ.get('INKSCAPE_PATH') or shutil.which('inkscape') or shutil.which('inkscape.exe')
    if not inkscape:
        return False
    # Use Inkscape CLI (>=1.0) - export type PNG and set width
    try:
        subprocess.check_call([
            inkscape,
            str(src),
            f"--export-filename={dst}",
            f"--export-width={size}",
            f"--export-height={size}"
        ])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Inkscape render failed for {src}: {e}")
        return False


def ensure_out(dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export SVG variants to PNG previews.')
    parser.add_argument('--inkscape-path', help='Explicit path to Inkscape binary', default=None)
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for variant in VARIANTS:
        src = VARIANTS_DIR / f"{variant}.svg"
        if not src.exists():
            print(f"Variant SVG not found: {src}")
            continue
        for size in SIZES:
            out_variant_dir = OUT_DIR / variant
            out_variant_dir.mkdir(parents=True, exist_ok=True)
            dst = out_variant_dir / f"{size}.png"
            print(f"Rendering {src.name} -> {dst} ({size}px)")
            ok = render_with_cairosvg(src, dst, size)
            if not ok:
                ok = render_with_inkscape(src, dst, size, inkscape_cmd=args.inkscape_path)
            if not ok:
                print(f"Failed to render {src.name} at {size}px: no renderer available or renderer failed.")
    print("Done")

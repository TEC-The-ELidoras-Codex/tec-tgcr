"""Convert SVG to PNG using cairosvg or Pillow fallback.
Touches ψʳ (structure) by producing deployment-ready visual assets.
"""

import argparse
import sys
from pathlib import Path

# Try cairosvg first (best quality)
try:
    import cairosvg

    HAS_CAIRO = True
except ImportError:
    HAS_CAIRO = False
    print("[WARN] cairosvg not installed; trying Pillow fallback", file=sys.stderr)

# Fallback to Pillow
try:
    from PIL import Image

    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


def svg_to_png_cairo(
    svg_path: Path, png_path: Path, width: int = 512, height: int = 512
):
    """Convert SVG to PNG using cairosvg (high quality)."""
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=width,
        output_height=height,
    )
    print(f"[ELY] Exported (cairosvg): {png_path}")


def svg_to_png_pillow(
    svg_path: Path, png_path: Path, width: int = 512, height: int = 512
):
    """Convert SVG to PNG using Pillow (basic fallback)."""
    # Pillow doesn't natively support SVG; needs external tool or rasterization
    # This is a placeholder; in practice, you'd use a browser or external renderer
    print(
        "[ERROR] Pillow cannot render SVG natively. Install cairosvg or use manual export.",
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert SVG to PNG with cairosvg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default=Path(__file__).parent.parent
        / "data/digital_assets/brand/svg/luminai_notion_emblem.svg",
        help="Input SVG path (default: luminai_notion_emblem.svg)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path(__file__).parent.parent
        / "data/digital_assets/brand/png/luminai_notion_emblem.png",
        help="Output PNG path (default: data/digital_assets/brand/png/luminai_notion_emblem.png)",
    )
    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=512,
        help="Output width in pixels (default: 512)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=None,
        help="Output height in pixels (default: same as width)",
    )

    args = parser.parse_args()

    svg_path = args.input
    png_path = args.output
    width = args.width
    height = args.height if args.height else width

    if not svg_path.exists():
        print(f"[ERROR] SVG not found: {svg_path}", file=sys.stderr)
        sys.exit(1)

    png_path.parent.mkdir(parents=True, exist_ok=True)

    if HAS_CAIRO:
        svg_to_png_cairo(svg_path, png_path, width, height)
    elif HAS_PILLOW:
        svg_to_png_pillow(svg_path, png_path, width, height)
    else:
        print("[ERROR] No SVG converter available. Install cairosvg:", file=sys.stderr)
        print("  pip install cairosvg", file=sys.stderr)
        sys.exit(1)

    if png_path.exists():
        size_kb = png_path.stat().st_size / 1024
        print(f"[ELY] PNG ready: {png_path} ({size_kb:.1f} KB, {width}×{height})")
    else:
        print("[ERROR] PNG export failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

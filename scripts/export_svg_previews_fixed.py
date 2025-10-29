"""
Render SVG variants to PNG previews after inlining CSS variables and removing unsupported filter attributes.
This script uses cairosvg directly and writes outputs to data/digital_assets/brand/preview/{variant}/{size}.png
"""
from pathlib import Path
import re
import cairosvg

BASE = Path(__file__).resolve().parents[1]
VARIANTS_DIR = BASE / 'data' / 'digital_assets' / 'brand' / 'svg'
OUT_DIR = BASE / 'data' / 'digital_assets' / 'brand' / 'preview'
SIZES = [1024, 512, 256, 120]
VARIANTS = ['luminai_mascot_logo', 'luminai_mascot_logo_tight', 'luminai_mascot_logo_inset']

# replacements for CSS variables used in the SVGs
REPLACEMENTS = {
    'var(--navy)': '#0B1E3B',
    'var(--violet)': '#6A00F4',
    'var(--cyan)': '#00D5C4',
    'var(--gold)': '#F2C340',
    'var(--white)': '#FFFFFF'
}

FILTER_RE = re.compile(r'\sfilter="url\(#[-a-zA-Z0-9_]+\)"')


def inline_and_clean(src: Path, dst: Path):
    s = src.read_text(encoding='utf-8')
    # inline CSS variables
    for var, val in REPLACEMENTS.items():
        s = s.replace(var, val)
    # remove filter attributes that can cause rendering failures
    s = FILTER_RE.sub('', s)
    # write to dst
    dst.write_text(s, encoding='utf-8')


if __name__ == '__main__':
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp_dir = OUT_DIR / 'tmp_svg'
    tmp_dir.mkdir(parents=True, exist_ok=True)

    for variant in VARIANTS:
        src = VARIANTS_DIR / f"{variant}.svg"
        if not src.exists():
            print(f"Variant SVG not found: {src}")
            continue
        for size in SIZES:
            out_variant_dir = OUT_DIR / variant
            out_variant_dir.mkdir(parents=True, exist_ok=True)
            dst = out_variant_dir / f"{size}.png"
            tmp_svg = tmp_dir / f"{variant}_tmp.svg"
            print(f"Rendering {src.name} -> {dst} ({size}px)")
            try:
                inline_and_clean(src, tmp_svg)
                cairosvg.svg2png(url=str(tmp_svg), write_to=str(dst), output_width=size, output_height=size)
                print(f"Rendered {dst}")
            except Exception as e:
                print(f"Failed to render {src.name} at {size}px: {e}")
    print("Done")

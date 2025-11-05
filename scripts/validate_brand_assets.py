#!/usr/bin/env python3
"""Simple validator for brand SVG assets.

Checks each SVG under config/brand/svg/ for presence of <title> and <desc>.
Exits with code 0 if all OK, 2 if any missing.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / 'config' / 'brand' / 'svg'

def check_svg(path: Path):
    text = path.read_text(encoding='utf-8')
    has_title = '<title' in text
    has_desc = '<desc' in text
    return has_title, has_desc

def main():
    if not SVG_DIR.exists():
        print(f'No SVG directory found at {SVG_DIR}', file=sys.stderr)
        sys.exit(2)

    failures = []
    for svg in sorted(SVG_DIR.glob('*.svg')):
        has_title, has_desc = check_svg(svg)
        if not (has_title and has_desc):
            failures.append((svg.name, has_title, has_desc))
            print(f'FAIL: {svg.name} — title: {has_title}, desc: {has_desc}')
        else:
            print(f'OK: {svg.name} — title and desc present')

    if failures:
        print('\nOne or more SVG assets are missing required accessibility metadata.', file=sys.stderr)
        sys.exit(2)
    print('\nAll SVG assets passed basic accessibility checks.')
    sys.exit(0)

if __name__ == '__main__':
    main()

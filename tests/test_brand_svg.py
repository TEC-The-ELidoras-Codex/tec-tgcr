from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "data" / "digital_assets" / "brand" / "svg" / "tec_resonance_logo.svg"


def test_resonance_logo_exists():
    assert SVG.exists(), f"Missing SVG: {SVG}"


def test_resonance_logo_basic_structure():
    text = SVG.read_text(encoding="utf-8")
    # Must be vector SVG with a 512x512 viewbox
    assert "viewBox=\"0 0 512 512\"" in text
    # Must include brand CSS variables
    assert "--color-deep-space" in text
    assert "--color-nexus-purple" in text
    assert "--color-cyber-gold" in text
    assert "--color-copper-glow" in text
    # Must be logically grouped
    assert "id=\"background\"" in text
    assert "id=\"core-geometry\"" in text
    assert "id=\"accents\"" in text
    assert "id=\"text\"" in text

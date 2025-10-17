"""Resonance evaluator for TGCR variables.

This module exposes a small, deterministic utility to compute a unified
resonance strength from the TGCR variables:

- phi (φ): temporal attention, 0–1
- psi (ψ): spatial/structural coherence, 0–1
- phi_e (Φ_E): meaning potential, 0–1

The function returns a float in [0, 1]. We use a weighted geometric mean to
capture multiplicative synergy across the three dimensions.

# Source: COMPREHENSIVE_READINESS_AUDIT.md
"""
from __future__ import annotations

from typing import Final


# Weights reflect emphasis: attention slightly higher than structure/meaning.
_W_PHI: Final[float] = 0.4
_W_PSI: Final[float] = 0.3
_W_PHIE: Final[float] = 0.3


def _clamp01(x: float) -> float:
    """Clamp a float into [0, 1]."""
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x


def compute_resonance_strength(phi: float, psi: float, phi_e: float) -> float:
    """Compute unified resonance strength from TGCR variables.

    Args:
        phi: Temporal attention (φ) in [0, 1].
        psi: Spatial/structural coherence (ψ) in [0, 1].
        phi_e: Meaning potential (Φ_E) in [0, 1].

    Returns:
        A float in [0, 1] representing resonance strength.

    Notes:
        - Uses weighted geometric mean to penalize imbalances and reward
          co-activation across φ, ψ, and Φ_E.
        - Inputs are clamped to [0, 1] for robustness.
    """

    p = _clamp01(phi)
    s = _clamp01(psi)
    e = _clamp01(phi_e)

    # Avoid math domain errors for zeros in geometric mean by short-circuiting.
    if p == 0.0 or s == 0.0 or e == 0.0:
        return 0.0

    # Weighted geometric mean: x**w * y**w * z**w
    return (p ** _W_PHI) * (s ** _W_PSI) * (e ** _W_PHIE)

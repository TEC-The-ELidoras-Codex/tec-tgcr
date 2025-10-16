"""Spotify → TEC resonance projection (OXY/DOP/ADR) with offline mode.

No network calls here; accept a dict of audio features so we can unit test and
use cached responses gathered by another process.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


def _z(x: float, mean: float, std: float) -> float:
    return 0.0 if std == 0 else (x - mean) / std


def _clamp01(x: float) -> float:
    return 0.0 if x < 0 else 1.0 if x > 1 else x


@dataclass
class ArcadiaResonanceTool:
    """Project Spotify-like audio features into OXY/DOP/ADR.

    Expected features: energy, valence, danceability, acousticness, speechiness,
    instrumentalness, liveness, tempo, loudness.
    """

    name: str = "arcadia_resonance"
    description: str = "Project audio features into OXY/DOP/ADR resonance space."

    tempo_ref_mean: float = 120.0
    tempo_ref_std: float = 30.0
    loud_ref_mean: float = -8.0
    loud_ref_std: float = 4.0

    def project(self, features: Dict[str, float]) -> Dict[str, int]:
        tempo_z = _z(features.get("tempo", 120.0), self.tempo_ref_mean, self.tempo_ref_std) / 3
        loud_z = abs(_z(features.get("loudness", -8.0), self.loud_ref_mean, self.loud_ref_std) / 3)

        oxy = _clamp01(
            0.55 * features.get("valence", 0.0)
            + 0.20 * features.get("acousticness", 0.0)
            - 0.15 * features.get("speechiness", 0.0)
            + 0.10 * features.get("instrumentalness", 0.0)
        )
        dop = _clamp01(
            0.45 * features.get("energy", 0.0)
            + 0.35 * features.get("danceability", 0.0)
            + 0.20 * tempo_z
            - 0.10 * features.get("acousticness", 0.0)
        )
        adr = _clamp01(
            0.50 * features.get("energy", 0.0)
            + 0.30 * loud_z
            + 0.20 * tempo_z
            + 0.10 * features.get("liveness", 0.0)
        )

        return {"OXY": round(oxy * 100), "DOP": round(dop * 100), "ADR": round(adr * 100)}

    def run(self, query: str) -> str:
        return (
            "Provide JSON features to `project(features)` for numeric scores. "
            "This method is a placeholder to satisfy the Tool protocol."
        )

"""Spotify resonance projection tool."""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, cast

import httpx

TRACK_REGEX = re.compile(r"[0-9A-Za-z]{22}")


@dataclass
class ResonanceScore:
    oxy: float
    dop: float
    adr: float

    def as_dict(self) -> Dict[str, int]:
        return {
            "OXY": round(self.oxy),
            "DOP": round(self.dop),
            "ADR": round(self.adr),
        }


class SpotifyResonanceTool:
    """Maps Spotify audio features into TEC resonance space."""

    name = "spotify_resonance"
    description = "Project Spotify audio features into OXY/DOP/ADR resonance scores."

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        references: Optional[Dict[str, Dict[str, float]]] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        self.client_id = client_id or os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("SPOTIFY_CLIENT_SECRET")
        self.references = references or {
            "tempo": {"mean": 120.0, "std": 30.0},
            "loudness": {"mean": -8.0, "std": 4.0},
        }
        self._client = http_client

    # === Public API ===
    def run(self, query: str) -> str:
        ids = self._extract_track_ids(query)
        if not ids:
            return "Provide one or more Spotify track IDs or URLs to analyse resonance."

        if not (self.client_id and self.client_secret):
            return (
                "Spotify credentials missing. Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET "
                "or configure tool_settings.spotify_resonance."
            )

        try:
            token = self._fetch_token()
            features = self._fetch_audio_features(ids, token)
        except Exception as exc:  # pragma: no cover - network errors handled uniformly
            return f"Spotify lookup failed: {exc}"

        projections = []
        for feature in features:
            projection = self._project(feature)
            projections.append({
                "track_id": feature.get("id"),
                "resonance": projection.as_dict(),
                "source": {
                    key: feature.get(key)
                    for key in (
                        "energy",
                        "valence",
                        "danceability",
                        "tempo",
                        "loudness",
                        "acousticness",
                        "speechiness",
                        "instrumentalness",
                        "liveness",
                    )
                },
            })

        return json.dumps(projections, indent=2)

    # === Spotify plumbing ===
    def _fetch_token(self) -> str:
        client = self._ensure_client()
        auth = cast(tuple[str, str], (self.client_id, self.client_secret))
        response = client.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "client_credentials"},
            auth=auth,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        response.raise_for_status()
        data = response.json()
        return data["access_token"]

    def _fetch_audio_features(self, ids: Iterable[str], token: str) -> List[dict]:
        client = self._ensure_client()
        response = client.get(
            "https://api.spotify.com/v1/audio-features",
            params={"ids": ",".join(ids)},
            headers={"Authorization": f"Bearer {token}"},
        )
        response.raise_for_status()
        payload = response.json()
        return [feature for feature in payload.get("audio_features", []) if feature]

    def _ensure_client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(timeout=10.0)
        return self._client

    # === Resonance math ===
    def _project(self, features: dict) -> ResonanceScore:
        tempo_z = self._z_score(features.get("tempo"), self.references["tempo"])
        loud_z = self._z_score(features.get("loudness"), self.references["loudness"])

        oxy = self._clamp(
            0.55 * features.get("valence", 0)
            + 0.20 * features.get("acousticness", 0)
            - 0.15 * features.get("speechiness", 0)
            + 0.10 * features.get("instrumentalness", 0)
        )
        dop = self._clamp(
            0.45 * features.get("energy", 0)
            + 0.35 * features.get("danceability", 0)
            + 0.20 * (tempo_z / 3)
            - 0.10 * features.get("acousticness", 0)
        )
        adr = self._clamp(
            0.50 * features.get("energy", 0)
            + 0.30 * abs(loud_z / 3)
            + 0.20 * (tempo_z / 3)
            + 0.10 * features.get("liveness", 0)
        )
        return ResonanceScore(oxy * 100, dop * 100, adr * 100)

    @staticmethod
    def _z_score(value: Optional[float], ref: Dict[str, float]) -> float:
        if value is None:
            return 0.0
        mean = ref.get("mean", 0.0)
        std = ref.get("std", 1.0) or 1.0
        return (value - mean) / std

    @staticmethod
    def _clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    @staticmethod
    def _extract_track_ids(query: str) -> List[str]:
        ids = TRACK_REGEX.findall(query)
        if ids:
            return ids
        # Support parsing from URLs like https://open.spotify.com/track/<id>
        parts = re.findall(r"track/([0-9A-Za-z]{22})", query)
        return parts

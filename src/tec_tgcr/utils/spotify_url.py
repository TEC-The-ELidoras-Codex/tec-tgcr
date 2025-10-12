from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs, urlencode

_SPOTIFY_HOSTS = {"open.spotify.com", "spotify.link", "spotify.app.link"}

_SPOTIFY_RE = re.compile(
    r"^(?:https?://)?(?:open\.)?spotify\.com/(?P<type>track|album|playlist|artist|episode|show)/(?P<id>[A-Za-z0-9]+)",
    re.IGNORECASE,
)

_SPOTIFY_PATH_RE = re.compile(
    r"/(?P<type>track|album|playlist|artist|episode|show)/(?P<id>[A-Za-z0-9]+)",
    re.IGNORECASE,
)

@dataclass(frozen=True)
class SpotifyUrl:
    kind: str
    id: str

    @property
    def canonical(self) -> str:
        return f"https://open.spotify.com/{self.kind}/{self.id}"

    @property
    def embed(self) -> str:
        return f"https://open.spotify.com/embed/{self.kind}/{self.id}"

SUPPORTED_TYPES = {"track", "album", "playlist", "artist", "episode", "show"}


def _coerce_shortlink(url: str) -> str:
    """Normalize common shortlink hosts to open.spotify.com when possible.
    We do not follow network redirects; just rewrite obvious patterns.
    """
    # Known patterns from share sheet sometimes include query tracking.
    if "spotify.link" in url or "spotify.app.link" in url:
        # Best effort: parse path and coerce to open.spotify.com
        parsed = urlparse(url if url.lower().startswith(("http://", "https://")) else "https://" + url)
        m = _SPOTIFY_PATH_RE.search(parsed.path or "")
        if m:
            return f"https://open.spotify.com/{m.group('type').lower()}/{m.group('id')}"
        # Fallback: return as-is; caller may still pass through parser
        return url
    return url


def parse_spotify_url(url: str) -> SpotifyUrl:
    """Parse a Spotify URL into its canonical parts, stripping tracking params.

    Accepts full URLs, mobile links, and short links. Raises ValueError if not
    a supported Spotify content URL.
    """
    if not isinstance(url, str) or not url.strip():
        raise ValueError("Empty URL")

    url = url.strip()
    url = _coerce_shortlink(url)

    # Ensure scheme for urlparse
    if not url.lower().startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)
    host = parsed.hostname or ""

    if not any(h in host for h in _SPOTIFY_HOSTS) and not host.endswith("spotify.com"):
        raise ValueError("Not a Spotify URL")

    m = _SPOTIFY_RE.search(url)
    if not m:
        raise ValueError("Unsupported Spotify path. Expected /{type}/{id}.")

    kind = m.group("type").lower()
    sid = m.group("id")

    if kind not in SUPPORTED_TYPES:
        raise ValueError(f"Unsupported Spotify type: {kind}")

    return SpotifyUrl(kind=kind, id=sid)


def sanitize_spotify_url(url: str) -> dict:
    """Return canonical and embed URLs for a given Spotify URL.

    Response shape:
    {
      "kind": "track|album|playlist|artist|episode|show",
      "id": "...",
      "canonical_url": "https://open.spotify.com/...",
      "embed_url": "https://open.spotify.com/embed/..."
    }
    """
    su = parse_spotify_url(url)
    return {
        "kind": su.kind,
        "id": su.id,
        "canonical_url": su.canonical,
        "embed_url": su.embed,
    }

from __future__ import annotations

import pytest

from tec_tgcr.utils.spotify_url import parse_spotify_url, sanitize_spotify_url


@pytest.mark.parametrize(
    "input_url,kind",
    [
        ("https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P", "track"),
        ("open.spotify.com/album/1ATL5GLyefJaxhQzSPVrLX", "album"),
        ("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=abc", "playlist"),
        ("https://spotify.link/track/7ouMYWpwJ422jRcDASZB7P", "track"),
    ],
)
def test_parse_spotify_url(input_url: str, kind: str):
    su = parse_spotify_url(input_url)
    assert su.kind == kind
    assert len(su.id) >= 10


def test_sanitize_outputs_canonical_and_embed():
    data = sanitize_spotify_url(
        "https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P?si=foo"
    )
    assert data["canonical_url"].startswith("https://open.spotify.com/track/")
    assert data["embed_url"].startswith("https://open.spotify.com/embed/track/")


def test_invalid_url_raises():
    with pytest.raises(ValueError):
        parse_spotify_url("https://example.com/foo")
    with pytest.raises(ValueError):
        parse_spotify_url("")

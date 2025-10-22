# AIRTH Lyrics Module — Technical and Legal Specification

This document defines a minimal, compliant approach for looking up lyrics for AIRTH without storing copyrighted text unlawfully.

## Goals
- Provide best-effort lyric discovery with proper attribution and licensing.
- Never cache or store full unlicensed lyrics in the repo or logs.
- Offer fallbacks and user-visible messaging when lyrics cannot be shown.

## Sources (in order)
1. Licensed APIs (recommended):
   - Musixmatch (commercial; provides licensing and attribution terms)
   - Genius API (terms vary; often returns metadata and snippets)
2. Openly licensed community sources:
   - LRCLIB (timed lyrics; CC0-like; verify source song match)
3. User-provided lyrics with proof of rights
4. Last resort: Link out to official lyric pages (do not display text)

## API usage posture
- Require API keys via environment variables (e.g., AIRTH_MUSIXMATCH_KEY)
- Rate-limit requests and respect robots/ToS
- Store only minimal fields: source, url, track metadata, and an excerpt ≤ 300 chars if ToS permits
- Always include attribution and link to the source page

## Data model (proposed)
```
LyricResult {
  track_id: str
  title: str
  artist: str
  album?: str
  source: "musixmatch" | "genius" | "lrclib" | "user" | "link-only"
  url?: str
  excerpt?: str  # ≤ 300 chars, only if ToS allows
  timecoded?: bool
  license?: str  # SPDX id or human-readable
  attribution?: str
}
```

## Behavior
- Query by track metadata (title/artist) or canonical Spotify ID (use scripts/sanitize_spotify_url.* to normalize)
- Prefer exact matches; if multiple candidates, present a short list
- If no licensed text is available, return a link-only result with attribution
- Do not persist full lyrics to disk unless license permits and user opted in

## UI/UX messaging
- When excerpts are shown: “Excerpt under license from <source> — full lyrics at <url>”
- When link-only: “Lyrics available at <source>. We link to respect licensing.”
- When none found: “No licensed lyrics found. Try refining the title/artist or provide authorized text.”

## Caching
- Cache only non-text metadata and the decision result (e.g., link-only). Include TTL (e.g., 24h) and hash of query.

## Error states
- Network/API error: return a structured error with retryAfter or suggestion
- Ambiguous result: return top-N with confidence scores
- Policy block: return a policy error with rationale (e.g., ToS restriction)

## Minimal interface (Python)
```
class LyricsClient:
    def lookup(self, *, title: str | None = None, artist: str | None = None, spotify_id: str | None = None) -> LyricResult:
        ...
```

## Compliance checklist
- [ ] Keys in env only; no hard-coded secrets
- [ ] Respect ToS and rate limits
- [ ] No storage of full unlicensed text
- [ ] Clear attribution and links
- [ ] Fallback to link-only when uncertain

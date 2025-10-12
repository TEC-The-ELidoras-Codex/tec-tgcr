from __future__ import annotations

import json
import sys
from tec_tgcr.utils.spotify_url import sanitize_spotify_url


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("Usage: sanitize_spotify_url.py <spotify_url>", file=sys.stderr)
        return 2
    try:
        data = sanitize_spotify_url(argv[0])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

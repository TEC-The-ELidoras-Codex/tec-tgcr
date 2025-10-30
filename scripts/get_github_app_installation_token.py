"""Create a JWT for a GitHub App and exchange it for an installation access token.

Usage (local):
  1) Set environment variables (example ``.env.local``):
      APP_ID=2186310
      # PRIVATE_KEY should contain the full PEM text including BEGIN/END lines.
      # Example (literal newlines shown for clarity):
      # -----BEGIN PRIVATE KEY-----
      # MIIE... (base64)
      # -----END PRIVATE KEY-----
      INSTALLATION_ID=12345678

  2) Install dependencies:
      pip install PyJWT requests cryptography

  3) Run:
      python scripts/get_github_app_installation_token.py

This script prints an installation token and a curl example. Do NOT commit private keys
or secrets to version control; use GitHub Secrets for Actions instead.
"""

from __future__ import annotations

import os
import time
import typing as t

import requests
import jwt  # PyJWT


GITHUB_API = "https://api.github.com"


def load_private_key_from_env() -> str:
    key = os.environ.get("PRIVATE_KEY")
    if not key:
        raise EnvironmentError("PRIVATE_KEY not set in environment")
    return key


def make_jwt(app_id: str, private_key_pem: str) -> str:
    """Create a signed JWT for GitHub App authentication.

    app_id: GitHub App ID as string
    private_key_pem: full PEM text
    Returns the encoded JWT (as str)
    """
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + (9 * 60),  # 9 minutes expiry (must be <= 10 minutes)
        "iss": str(app_id),
    }
    token = jwt.encode(payload, private_key_pem, algorithm="RS256")
    # PyJWT 2.x returns str; older versions may return bytes
    if isinstance(token, bytes):
        token = token.decode()
    return token


def get_installation_id_from_app(jwt_token: str) -> int:
    """Query the App installations to choose an installation ID if not provided."""
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
    }
    resp = requests.get(f"{GITHUB_API}/app/installations", headers=headers)
    resp.raise_for_status()
    data = resp.json()
    if not isinstance(data, list) or not data:
        raise RuntimeError("No installations found for the App")
    # Return first installation id by default
    return int(data[0]["id"])


def create_installation_token(
    jwt_token: str, installation_id: int
) -> t.Dict[str, t.Any]:
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
    }
    resp = requests.post(
        f"{GITHUB_API}/app/installations/{installation_id}/access_tokens",
        headers=headers,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    app_id = os.environ.get("APP_ID")
    if not app_id:
        raise SystemExit("Please set APP_ID in the environment")

    private_key = load_private_key_from_env()

    print("Creating JWT...")
    jwt_token = make_jwt(app_id, private_key)

    installation_id_env = os.environ.get("INSTALLATION_ID")
    if installation_id_env:
        installation_id = int(installation_id_env)
    else:
        print("No INSTALLATION_ID set — querying installations for the App...")
        installation_id = get_installation_id_from_app(jwt_token)
        print(f"Using installation id: {installation_id}")

    print("Requesting installation token...")
    token_response = create_installation_token(jwt_token, installation_id)

    token = token_response.get("token")
    expires_at = token_response.get("expires_at")

    print("\n=== Installation token ===")
    print(token)
    print("Expires at:", expires_at)

    print("\nUse example (curl):")
    print(
        f'curl -H "Authorization: Bearer {token}" -H "Accept: application/vnd.github+json" https://api.github.com/user'
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
        raise

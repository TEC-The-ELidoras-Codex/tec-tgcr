from __future__ import annotations

from rich.console import Console
from tec_tgcr.env import env_str, env_path

console = Console()

KEYS = [
    "CIVITAI_API_KEY",
    "WORLDANVIL_API_KEY",
    "ORCID_ID",
]

PATHS = [
    "SD_ROOT_DIR",
    "SD_CHECKPOINT_DIR",
    "SD_CONTROLNET_DIR",
    "SD_UPSCALER_DIR",
    "SD_HYPERNET_DIR",
    "SD_EMBEDDING_DIR",
    "SD_LORA_DIR",
    "SD_LYCORIS_DIR",
    "SD_VAE_DIR",
    "SD_DORA_DIR",
]


def main() -> None:
    console.rule("Environment Check")
    for k in KEYS:
        v = env_str(k)
        status = "SET" if v else "MISSING"
        console.print(f"[bold]{k}[/bold]: {status}")
    console.print()
    for p in PATHS:
        path = env_path(p)
        status = (
            "OK" if path.exists() else ("NOT SET" if str(path) == "" else "MISSING")
        )
        console.print(f"[bold]{p}[/bold]: {path} -> {status}")


if __name__ == "__main__":
    main()

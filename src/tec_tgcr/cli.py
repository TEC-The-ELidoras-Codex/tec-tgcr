"""Command line interface for interacting with TEC agents."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.prompt import Prompt

from .agents.airth import AirthResearchGuard
from .config import AgentConfig
from .integrations.civitai import CivitaiClient
from .integrations.worldanvil import WorldAnvilClient
from .session import ConversationSession
from .tools.resonance_evaluator import compute_resonance_strength
from .tools import notion as notion_tools

console = Console()
app = typer.Typer(help="Operate the TEC conversational agents.")


@app.command()
def chat(
    config_path: Optional[Path] = typer.Option(
        None,
        "--config",
        "-c",
        help="Optional path to an agent configuration YAML file.",
    ),
    prompt: Optional[str] = typer.Argument(None, help="Optional initial user prompt."),
) -> None:
    """Run an interactive chat session with the Airth Research Guard agent."""

    if config_path is not None and not config_path.exists():
        raise typer.BadParameter(f"Config file not found: {config_path}")

    config = AgentConfig.load(config_path)
    agent = AirthResearchGuard(config=config)
    session = ConversationSession(agent=agent)

    console.print("[bold magenta]Airth Research Guard engaged.[/bold magenta]")
    console.print("Type 'exit' to end the conversation.\n")

    if prompt:
        console.print(f"[bold cyan]You:[/bold cyan] {prompt}")
        response = session.process_user_message(prompt)
        console.print(f"[bold green]Airth:[/bold green] {response}")

    while True:
        user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
        if user_input.strip().lower() in {"exit", "quit"}:
            console.print("[bold magenta]Session terminated.[/bold magenta]")
            break
        response = session.process_user_message(user_input)
        console.print(f"[bold green]Airth:[/bold green] {response}")


@app.command()
def manifest(output: Path = typer.Argument(Path("agent_manifest.json"))) -> None:
    """Export the Airth Research Guard manifest to JSON."""
    config = AgentConfig.load()
    agent = AirthResearchGuard(config=config)

    manifest_data = agent.manifest()
    output.write_text(json.dumps(manifest_data, indent=2))
    console.print(f"Manifest exported to [bold]{output}[/bold]")


@app.command()
def civitai_search(query: str = typer.Argument(...), limit: int = 10) -> None:
    """Search Civitai models (requires CIVITAI_API_KEY for full access)."""
    client = CivitaiClient()
    results = client.list_models(query=query, limit=limit)
    console.print_json(data=results)


@app.command()
def worldanvil_me() -> None:
    """Test World Anvil authentication and print account info."""
    client = WorldAnvilClient()
    me = client.get_me()
    console.print_json(data=me)


if __name__ == "__main__":
    app()


@app.command()
def resonance_evaluate(
    phi: float = typer.Option(..., help="Temporal attention φ (0–1)"),
    psi: float = typer.Option(..., help="Spatial/structural coherence ψ (0–1)"),
    phi_e: float = typer.Option(..., help="Meaning potential Φ_E (0–1)"),
) -> None:
    """Evaluate resonance strength from TGCR variables.

    Returns a single score in [0, 1] using a weighted geometric mean.
    """

    strength = compute_resonance_strength(phi, psi, phi_e)
    console.print(f"Resonance strength: [bold]{strength:.3f}[/bold]")
    console.print(f"φ (attention): {phi:.3f}")
    console.print(f"ψ (structure): {psi:.3f}")
    console.print(f"Φ_E (meaning): {phi_e:.3f}")


@app.command()
def notion_health() -> None:
    """Check Notion API connectivity.

    Requires NOTION_TOKEN set and the integration shared with your workspace/pages.
    """
    ok, msg = notion_tools.health_check()
    if ok:
        console.print(f"[bold green]Notion health:[/bold green] {msg}")
    else:
        console.print(f"[bold red]Notion health failed:[/bold red] {msg}")
        raise typer.Exit(code=1)


@app.command()
def notion_search(query: str = typer.Argument(None), page_size: int = 10) -> None:
    """Search Notion for pages/databases (best-effort)."""
    try:
        data = notion_tools.search(query=query, page_size=page_size)
        console.print_json(data=data)
    except Exception as e:  # pragma: no cover - network path
        console.print(f"[bold red]Search failed:[/bold red] {e}")
        raise typer.Exit(code=1)

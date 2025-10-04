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
from .session import ConversationSession

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


if __name__ == "__main__":
    app()

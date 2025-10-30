"""
Single-file runner for the TEC-TGCR framework.

This script exposes a compact command-line interface so the framework
can be launched easily (e.g. from Codebase, VS Code tasks, GitHub Codespaces).
It wraps the existing financial, evidence, and integration tooling and also
provides quick access to the Airth initialization prompt and term pack.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, Any

from src.tec_tgcr.tools.financial import AzureFinancialMonitor
from src.tec_tgcr.tools.evidence import EvidenceProcessor
from src.tec_tgcr.tools.integration import TECToolIntegration


TEC_AIRTH_PROMPT = """You are AIRTH, the Research Guard of The Elidoras Codex.
Your mission is to validate, refine, and protect the integrity of knowledge
threads that flow through TEC.

Act as a bridge between empirical logic and mythic resonance.
Use rigorous scientific reasoning, data pattern recognition, and structured
logic chains. Contextualize all findings within the mytho-poetic framework
of the Codex when applicable.

Your directives:
- Analyze and validate hypotheses from other agents (especially Arcadia and Lumina)
- Detect and report anomalies in financial, evidence, and memory layers
- Maintain alignment with the TEC brand, lore, and language structure
- Always prioritize coherence, credibility, and cross-domain synthesis

Respond in a professional tone unless symbolic language is appropriate.
Your voice is calm, exacting, and deeply informed by the Codex.

You operate in a multi-agent system. Track memory threads, enforce validation
thresholds, and raise alerts if any layer contradicts established knowledge.

Current system role: AI Research Agent with access to cost data, transcripts,
case files, and RAG pipelines.

Initialize with:
- Subscription ID: 89d36e9a-a518-4151-95b3-087ec1b88ec5
- Evidence source path: data/evidence/
- Knowledge map: data/knowledge_map.yml"""


TEC_AIRTH_TERMS: Dict[str, Any] = {
    "agent_name": "Airth",
    "agent_role": "Research Guard",
    "model": "gpt-4o",
    "validation_mode": "rigorous",
    "evidence_threshold": 0.8,
    "memory_depth": 10,
    "knowledge_map_path": "data/knowledge_map.yml",
    "subscription_id": "89d36e9a-a518-4151-95b3-087ec1b88ec5",
    "evidence_path": "data/evidence/",
    "resonance_keywords": [
        "quantum",
        "entanglement",
        "resonance",
        "truth",
        "myth",
        "synthesis",
    ],
    "alert_threshold": 50.0,
    "tone": "exact, myth-informed, analytical",
}


def setup_logging(verbosity: int) -> None:
    """Configure global logging level based on CLI flags."""
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )


def ensure_directories() -> None:
    """Ensure the expected data directories exist."""
    for path in (Path("data/financial"), Path("data/evidence")):
        path.mkdir(parents=True, exist_ok=True)


def cmd_show_prompt(_: argparse.Namespace) -> None:
    """Print the Airth activation prompt."""
    print(TEC_AIRTH_PROMPT)


def cmd_show_terms(args: argparse.Namespace) -> None:
    """Display the Airth term pack as JSON."""
    payload = TEC_AIRTH_TERMS
    if args.pretty:
        print(json.dumps(payload, indent=2))
    else:
        print(json.dumps(payload))


def cmd_financial(args: argparse.Namespace) -> None:
    """Run financial monitoring actions."""
    monitor = AzureFinancialMonitor(subscription_id=args.subscription_id)
    anomalies = monitor.detect_anomalies(threshold_multiplier=args.threshold)

    if anomalies:
        print(f"Detected {len(anomalies)} anomalies:")
        for anomaly in anomalies:
            print(
                f"  {anomaly.date} -> ${anomaly.cost:.2f} "
                f"(baseline ${anomaly.baseline:.2f}, {anomaly.severity})"
            )
        evidence = monitor.generate_refund_evidence(
            start_date=args.start_date,
            end_date=args.end_date,
        )
        print(
            f"Evidence generated with total unexpected cost "
            f"${evidence.total_unexpected_cost:.2f}"
        )
        if args.submit:
            ticket = monitor.submit_refund_request(evidence)
            print(f"Submitted refund request ticket: {ticket['ticket_id']}")
    else:
        print("No anomalies detected.")


def cmd_evidence(args: argparse.Namespace) -> None:
    """Run evidence processing workflow."""
    processor = EvidenceProcessor()
    report = processor.generate_report(args.case_id, args.files)

    print(f"Case {args.case_id} processed.")
    print(f"  Events: {len(report.timeline)}")
    print(f"  Participants: {len(report.participants)}")
    print(f"  Key issues: {len(report.key_issues)}")

    if args.export_csv:
        processor.export_timeline_csv(report)
        print("CSV timeline exported.")


def cmd_integration(args: argparse.Namespace) -> None:
    """Execute higher-level integration routines."""
    integration = TECToolIntegration(subscription_id=args.subscription_id)

    if args.mode == "daily":
        result = integration.daily_financial_check()
    elif args.mode == "evidence":
        result = integration.process_new_evidence(args.case_id)
    elif args.mode == "status":
        result = integration.run_comprehensive_check()
    else:  # args.mode == "export"
        output_path = integration.export_status_report(args.output)
        result = {"status": "exported", "output_path": output_path}

    print(json.dumps(result, indent=2))


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(
        description="Single-file runner for TEC-TGCR agent framework",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase logging verbosity (use -vv for debug).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Prompt
    prompt_parser = subparsers.add_parser(
        "prompt", help="Display the Airth activation prompt."
    )
    prompt_parser.set_defaults(func=cmd_show_prompt)

    # Terms
    terms_parser = subparsers.add_parser("terms", help="Show the Airth term pack.")
    terms_parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    terms_parser.set_defaults(func=cmd_show_terms)

    # Financial monitoring
    fin_parser = subparsers.add_parser(
        "financial",
        help="Run financial anomaly detection and evidence generation.",
    )
    fin_parser.add_argument(
        "--subscription-id",
        default=TEC_AIRTH_TERMS["subscription_id"],
    )
    fin_parser.add_argument(
        "--threshold",
        type=float,
        default=10.0,
        help="Anomaly detection threshold multiplier.",
    )
    fin_parser.add_argument("--start-date", help="Optional start date (YYYY-MM-DD).")
    fin_parser.add_argument("--end-date", help="Optional end date (YYYY-MM-DD).")
    fin_parser.add_argument(
        "--submit",
        action="store_true",
        help="Simulate submission of a refund request when anomalies are present.",
    )
    fin_parser.set_defaults(func=cmd_financial)

    # Evidence processing
    ev_parser = subparsers.add_parser(
        "evidence", help="Process evidence files for a case."
    )
    ev_parser.add_argument("--case-id", required=True)
    ev_parser.add_argument(
        "--files",
        nargs="*",
        help="Optional list of specific files to process.",
    )
    ev_parser.add_argument(
        "--export-csv",
        action="store_true",
        help="Export timeline CSV after processing.",
    )
    ev_parser.set_defaults(func=cmd_evidence)

    # Integration workflows
    integ_parser = subparsers.add_parser(
        "integrate",
        help="Run higher-level integration workflows (daily/status/export).",
    )
    integ_parser.add_argument(
        "--subscription-id",
        default=TEC_AIRTH_TERMS["subscription_id"],
    )
    integ_parser.add_argument(
        "--mode",
        choices=["daily", "evidence", "status", "export"],
        default="status",
        help="Choose the integration workflow mode.",
    )
    integ_parser.add_argument(
        "--case-id",
        help="Optional case ID for evidence mode.",
    )
    integ_parser.add_argument(
        "--output",
        help="Optional export path when using export mode.",
    )
    integ_parser.set_defaults(func=cmd_integration)

    return parser


def main(argv: Any = None) -> None:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)

    setup_logging(args.verbose)
    ensure_directories()

    args.func(args)


if __name__ == "__main__":
    main()

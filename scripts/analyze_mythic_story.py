#!/usr/bin/env python3
"""Generate structural insights for the mythic resonance map."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence


@dataclass
class NodeSummary:
    node_id: str
    label: str
    fill: str
    indegree: int
    outdegree: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("docs/resonance_map/figma_nodes_edges.json"),
        help="Path to the mythic story node/edge JSON export.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/resonance_conscience/analysis/mythic_story_analysis.md"),
        help="Path to write the generated Markdown analysis.",
    )
    return parser.parse_args()


def load_payload(path: Path) -> Dict:
    if not path.exists():
        raise FileNotFoundError(f"Input data not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_adjacency(edges: Sequence[Dict]) -> Dict[str, List[str]]:
    adjacency: Dict[str, List[str]] = defaultdict(list)
    for edge in edges:
        origin = edge["from"]
        target = edge["to"]
        if edge.get("style") == "dotted":
            # Exclude dotted edges from structural cycles; they act as soft guidance.
            continue
        adjacency[origin].append(target)
        if edge.get("bidirectional"):
            adjacency[target].append(origin)
    return adjacency


def build_reversed(adjacency: Dict[str, List[str]]) -> Dict[str, List[str]]:
    reversed_adj: Dict[str, List[str]] = defaultdict(list)
    for origin, targets in adjacency.items():
        for target in targets:
            reversed_adj[target].append(origin)
    return reversed_adj


def kosaraju_components(adjacency: Dict[str, List[str]]) -> List[List[str]]:
    visited: Dict[str, bool] = {}
    order: List[str] = []

    def dfs(node: str) -> None:
        visited[node] = True
        for neighbor in adjacency.get(node, []):
            if not visited.get(neighbor):
                dfs(neighbor)
        order.append(node)

    for node in adjacency:
        if not visited.get(node):
            dfs(node)

    reversed_adj = build_reversed(adjacency)
    visited.clear()
    components: List[List[str]] = []

    def dfs_rev(node: str, bucket: List[str]) -> None:
        visited[node] = True
        bucket.append(node)
        for neighbor in reversed_adj.get(node, []):
            if not visited.get(neighbor):
                dfs_rev(neighbor, bucket)

    for node in reversed(order):
        if not visited.get(node):
            component: List[str] = []
            dfs_rev(node, component)
            components.append(component)

    return [component for component in components if len(component) > 1]


def summarize_nodes(data: Dict) -> Dict[str, NodeSummary]:
    indegree = Counter()
    outdegree = Counter()
    for edge in data["edges"]:
        origin = edge["from"]
        target = edge["to"]
        outdegree[origin] += 1
        indegree[target] += 1
        if edge.get("bidirectional"):
            outdegree[target] += 1
            indegree[origin] += 1

    summaries: Dict[str, NodeSummary] = {}
    for node in data["nodes"]:
        node_id = node["id"]
        summaries[node_id] = NodeSummary(
            node_id=node_id,
            label=node["label"],
            fill=node.get("fill", "unspecified"),
            indegree=indegree[node_id],
            outdegree=outdegree[node_id],
        )
    return summaries


def format_markdown(
    data: Dict,
    node_summaries: Dict[str, NodeSummary],
    components: Sequence[Sequence[str]],
) -> str:
    total_nodes = len(node_summaries)
    total_edges = len(data["edges"])
    dotted_edges = sum(1 for edge in data["edges"] if edge.get("style") == "dotted")
    fill_counts = Counter(summary.fill for summary in node_summaries.values())

    archetype_nodes = [summary for summary in node_summaries.values() if "—" in summary.label]
    archetype_nodes.sort(key=lambda item: item.outdegree + item.indegree, reverse=True)

    deg_sorted = sorted(
        node_summaries.values(),
        key=lambda summary: (summary.outdegree + summary.indegree, summary.label),
        reverse=True,
    )

    lines = []
    lines.append("# Mythic Story Network Analysis")
    lines.append("")
    lines.append("## Graph Overview")
    lines.append(f"- Nodes: {total_nodes}")
    lines.append(f"- Edges: {total_edges} (dotted guidance edges: {dotted_edges})")
    lines.append(f"- Halo label: {data.get('halo', {}).get('label', 'N/A')}")
    lines.append("")

    lines.append("## Fill Distribution")
    for fill, count in fill_counts.most_common():
        lines.append(f"- {fill}: {count}")
    lines.append("")

    lines.append("## Degree Leaderboard")
    lines.append("| Node | Label | Fill | In ↦ | Out ↤ | Total |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for summary in deg_sorted:
        total = summary.indegree + summary.outdegree
        safe_label = summary.label.replace("\n", " / ")
        lines.append(
            f"| `{summary.node_id}` | {safe_label} | {summary.fill} | {summary.indegree} | {summary.outdegree} | {total} |"
        )
    lines.append("")

    if archetype_nodes:
        lines.append("## Mythic Archetypes")
        lines.append("Characters encoded with em dash titles highlight narrative roles.")
        for summary in archetype_nodes:
            safe_label = summary.label.replace("\n", " / ")
            lines.append(f"- `{summary.node_id}` → {safe_label} (total degree {summary.indegree + summary.outdegree})")
        lines.append("")

    if components:
        lines.append("## Cyclical Components")
        lines.append("The following strongly connected components indicate feedback loops in the mythic system:")
        for component in components:
            labels = [node_summaries[node_id].label.replace("\n", " / ") for node_id in component]
            joined = ", ".join(f"`{node_id}` ({label})" for node_id, label in zip(component, labels))
            lines.append(f"- {joined}")
        lines.append("")

    lines.append("## Guidance Edges")
    if dotted_edges:
        lines.append("Dotted edges signal mentor-like influences or narrative foreshadowing:")
        for edge in data["edges"]:
            if edge.get("style") == "dotted":
                origin = node_summaries[edge["from"]].label.replace("\n", " / ")
                target = node_summaries[edge["to"]].label.replace("\n", " / ")
                lines.append(f"- `{edge['from']}` → `{edge['to']}` :: {origin} ⇒ {target}")
    else:
        lines.append("No dotted guidance edges detected in the dataset.")

    lines.append("")
    lines.append("_Generated by `scripts/analyze_mythic_story.py`_")

    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    data = load_payload(args.input)
    node_summaries = summarize_nodes(data)
    adjacency = build_adjacency(data["edges"])
    components = kosaraju_components(adjacency)
    markdown = format_markdown(data, node_summaries, components)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"Mythic analysis written to {args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
CODEX Knowledge API Server
Serves 7 CODEX cards via REST API for ChatGPT Actions integration
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
CODEX_DIR = Path(__file__).parent.parent / "research" / "CODEX"
API_VERSION = "1.0"
SERVICE_NAME = "CODEX Knowledge Service"

# ============================================================================
# CARD MANIFEST (Update this if you add/remove cards)
# ============================================================================

CARD_MANIFEST = [
    {
        "slug": "codex_chronosphere",
        "filename": "CODEX_CHRONOSPHERE.md",
        "category": "core_theory",
        "title": "CODEX Chronosphere",
        "focus": "Time, thresholds, information cascades",
        "tgcr_alignment": {"phi_t": 9, "psi_r": 8, "phi_e": 9},
    },
    {
        "slug": "codex_pac_man_universe",
        "filename": "CODEX_PAC_MAN_UNIVERSE.md",
        "category": "core_theory",
        "title": "CODEX Pac-Man Universe",
        "focus": "Topology, loops, memory",
        "tgcr_alignment": {"phi_t": 8, "psi_r": 9, "phi_e": 8},
    },
    {
        "slug": "codex_steward_matter_subconscience_self",
        "filename": "CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF.md",
        "category": "core_theory",
        "title": "CODEX Steward/Matter/Subconscience/Self",
        "focus": "Ethical stewardship, matter, subconscious, identity",
        "tgcr_alignment": {"phi_t": 9, "psi_r": 9, "phi_e": 9},
    },
    {
        "slug": "codex_synthetic_introspection",
        "filename": "CODEX_SYNTHETIC_INTROSPECTION.md",
        "category": "nodes",
        "title": "CODEX Synthetic Introspection",
        "focus": "AI consciousness, resonance tests",
        "tgcr_alignment": {"phi_t": 8, "psi_r": 8, "phi_e": 7},
    },
    {
        "slug": "codex_gut_brain_phi_t",
        "filename": "CODEX_GUT_BRAIN_PHI_T.md",
        "category": "nodes",
        "title": "CODEX Gut-Brain Phi-T",
        "focus": "Embodied decision-making, vagal leadership",
        "tgcr_alignment": {"phi_t": 9, "psi_r": 7, "phi_e": 8},
    },
    {
        "slug": "codex_sleep_token_rain",
        "filename": "CODEX_SLEEP_TOKEN_RAIN.md",
        "category": "clusters",
        "title": "CODEX Sleep Token Rain",
        "focus": "Music as cosmic pattern (Sleep Token case)",
        "tgcr_alignment": {"phi_t": 8, "psi_r": 9, "phi_e": 8},
    },
    {
        "slug": "codex_tdwp",
        "filename": "CODEX_TDWP.md",
        "category": "clusters",
        "title": "CODEX TDWP",
        "focus": "Structural cadence (The Devil Wears Prada)",
        "tgcr_alignment": {"phi_t": 7, "psi_r": 9, "phi_e": 7},
    },
]


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def load_card_content(slug: str) -> str | None:
    """Load full markdown content of a card by slug."""
    card = next((c for c in CARD_MANIFEST if c["slug"] == slug), None)
    if not card:
        return None

    path = CODEX_DIR / card["category"] / card["filename"]
    if path.exists():
        return path.read_text()
    return None


def get_card_metadata(slug: str) -> Dict[str, Any] | None:
    """Get metadata for a card without loading full content."""
    return next((c for c in CARD_MANIFEST if c["slug"] == slug), None)


def score_relevance(question: str, cards: List[Dict]) -> List[tuple]:
    """
    Simple relevance scoring for question-to-card mapping.
    Returns list of (card, score) tuples sorted by relevance.
    """
    question_lower = question.lower()
    scored = []

    for card in cards:
        score = 0

        # Check focus keywords
        if card["focus"].lower() in question_lower:
            score += 3

        # Check title
        if card["slug"].lower() in question_lower:
            score += 2

        # Check partial matches
        focus_words = card["focus"].lower().split()
        for word in focus_words:
            if len(word) > 3 and word in question_lower:
                score += 1

        if score > 0:
            scored.append((card, score))

    return sorted(scored, key=lambda x: x[1], reverse=True)


# ============================================================================
# API ENDPOINTS
# ============================================================================


@app.route("/api/v1/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify(
        {
            "status": "ok",
            "service": SERVICE_NAME,
            "version": API_VERSION,
            "cards_available": len(CARD_MANIFEST),
        }
    )


@app.route("/api/v1/cards", methods=["GET"])
def list_cards():
    """List all CODEX cards with metadata."""
    search = request.args.get("search", "").lower()

    cards = CARD_MANIFEST

    # Filter by search if provided
    if search:
        cards = [
            c
            for c in cards
            if search in c["slug"]
            or search in c["title"].lower()
            or search in c["focus"].lower()
        ]

    return jsonify(
        {
            "cards": cards,
            "count": len(cards),
            "total_available": len(CARD_MANIFEST),
        }
    )


@app.route("/api/v1/cards/<slug>", methods=["GET"])
def get_card(slug: str):
    """Get full card content + metadata."""
    metadata = get_card_metadata(slug)

    if not metadata:
        return (
            jsonify({"error": "Card not found", "slug": slug, "available_cards": [c["slug"] for c in CARD_MANIFEST]}),
            404,
        )

    content = load_card_content(slug)

    if not content:
        return jsonify({"error": "Card file not found", "slug": slug}), 500

    return jsonify(
        {
            "slug": slug,
            "metadata": metadata,
            "content": content,
            "format": "markdown",
        }
    )


@app.route("/api/v1/cards/<slug>/section/<section>", methods=["GET"])
def get_card_section(slug: str, section: str):
    """Get a specific section of a card (e.g., examples, rituals)."""
    content = load_card_content(slug)

    if not content:
        return jsonify({"error": "Card not found"}), 404

    # Simple section extraction by heading
    section_lower = section.lower()
    lines = content.split("\n")
    section_content = []
    in_section = False

    for i, line in enumerate(lines):
        if section_lower in line.lower() and line.startswith("#"):
            in_section = True
            section_content.append(line)
        elif in_section and line.startswith("#"):
            # Hit next section
            break
        elif in_section:
            section_content.append(line)

    if not section_content:
        return (
            jsonify(
                {
                    "error": "Section not found",
                    "slug": slug,
                    "section": section,
                    "available_sections": ["examples", "rituals", "practices"],
                }
            ),
            404,
        )

    return jsonify(
        {
            "slug": slug,
            "section": section,
            "content": "\n".join(section_content),
            "format": "markdown",
        }
    )


@app.route("/api/v1/map-question", methods=["POST"])
def map_question_to_cards():
    """
    POWER ENDPOINT: Map a question to relevant CODEX cards.
    Returns ranked list of cards with confidence scores.
    """
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request body"}), 400

    question = data["question"]

    # Score all cards
    scored = score_relevance(question, CARD_MANIFEST)

    # Format response
    recommendations = [
        {
            "rank": i + 1,
            "slug": card["slug"],
            "title": card["title"],
            "focus": card["focus"],
            "confidence_score": score,
            "tgcr_alignment": card["tgcr_alignment"],
        }
        for i, (card, score) in enumerate(scored[:5])  # Top 5
    ]

    return jsonify(
        {
            "question": question,
            "recommendations": recommendations,
            "explanation": "Ranked by relevance to your question. Higher confidence = better match.",
        }
    )


@app.route("/api/v1/manifest", methods=["GET"])
def get_manifest():
    """Get complete knowledge manifest."""
    return jsonify(
        {
            "service": SERVICE_NAME,
            "version": API_VERSION,
            "cards": CARD_MANIFEST,
            "total_cards": len(CARD_MANIFEST),
            "core_framework": "TGCR (Theory of General Contextual Resonance)",
            "main_card": "CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF",
            "categories": list(set(c["category"] for c in CARD_MANIFEST)),
        }
    )


@app.route("/api/v1/quick-start", methods=["GET"])
def quick_start():
    """Get quick start guide for using CODEX."""
    return jsonify(
        {
            "quick_start": {
                "step_1": "Read CODEX_STEWARD_MATTER_SUBCONSCIENCE_SELF (foundation)",
                "step_2": "Explore CODEX_CHRONOSPHERE and CODEX_PAC_MAN_UNIVERSE (core theory)",
                "step_3": "Pick a node or cluster based on your interest",
                "step_4": "Use /map-question endpoint to find relevant cards for your research",
            },
            "endpoint_examples": {
                "list_all_cards": "GET /api/v1/cards",
                "get_card": "GET /api/v1/cards/codex_chronosphere",
                "search_cards": "GET /api/v1/cards?search=time",
                "map_question": "POST /api/v1/map-question with {'question': 'your question'}",
                "get_manifest": "GET /api/v1/manifest",
            },
        }
    )


@app.route("/api/v1/refinements", methods=["GET"])
def list_refinements():
    """List previous research refinements."""
    # TODO: Implement refinement logging
    return jsonify({"refinements": [], "message": "Refinement logging coming soon"})


@app.route("/api/v1/refinements", methods=["POST"])
def log_refinement():
    """Log a new refinement to CODEX."""
    data = request.get_json()

    # TODO: Implement refinement storage
    return jsonify(
        {
            "status": "received",
            "refinement": data,
            "message": "Refinement logging coming soon",
        }
    )


# ============================================================================
# ERROR HANDLERS
# ============================================================================


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found", "available_endpoints": ["/api/v1/health", "/api/v1/cards", "/api/v1/manifest"]}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    port = int(os.getenv("CODEX_API_PORT", 5000))
    debug = os.getenv("ENVIRONMENT") == "development"

    print(f"\n🚀 {SERVICE_NAME} v{API_VERSION}")
    print(f"📍 Starting on http://localhost:{port}")
    print(f"📚 Serving {len(CARD_MANIFEST)} CODEX cards")
    print(f"📖 Browse cards at http://localhost:{port}/api/v1/cards\n")

    app.run(debug=debug, host="0.0.0.0", port=port)

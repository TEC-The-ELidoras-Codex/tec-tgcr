"""REST API endpoints for auto-loaded knowledge assets.

Provides HTTP endpoints that serve personas, guides, classification, and system info
automatically loaded from source files. No manual uploads needed—changes to markdown
files automatically reflect in API responses.

Endpoints:
  GET /api/personas/              — List all 9 personas
  GET /api/personas/{name}        — Get specific persona spec
  GET /api/guides/                — List all deployment guides
  GET /api/guides/{guide_name}    — Get specific guide
  GET /api/classification/        — Get shareable/internal rules
  GET /api/system/                — Get system integration info
  GET /api/knowledge/             — Get all assets (unified knowledge base)

Usage:
    from tec_tgcr.integrations.knowledge_api import router
    app.include_router(router, prefix="/api")
    # GET http://localhost:8000/api/personas/
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from tec_tgcr.knowledge.asset_loader import get_loader

router = APIRouter(prefix="/api", tags=["knowledge"])


class AssetResponse(BaseModel):
    """Standard response for asset endpoints."""

    title: str
    content: str
    path: str
    metadata: dict = {}


class PersonaResponse(BaseModel):
    """Response containing a persona specification."""

    name: str
    title: str
    content: str
    path: str
    metadata: dict = {}


class PersonasListResponse(BaseModel):
    """Response containing list of personas with brief info."""

    personas: dict
    count: int
    status: str = "auto-synced"


class GuideResponse(BaseModel):
    """Response containing a deployment guide."""

    name: str
    title: str
    content: str
    path: str


class GuidesListResponse(BaseModel):
    """Response containing list of guides."""

    guides: dict
    count: int
    status: str = "auto-synced"


class ClassificationResponse(BaseModel):
    """Response containing shareable/internal classification rules."""

    title: str
    content: str
    path: str
    categories: dict


class SystemInfoResponse(BaseModel):
    """Response containing system integration guide and workflows."""

    title: str
    content: str
    path: str


class KnowledgeBaseResponse(BaseModel):
    """Complete unified knowledge base (all assets)."""

    personas: dict
    guides: dict
    classification: dict
    system: dict
    metadata: dict


# ============================================================================
# PERSONAS ENDPOINTS
# ============================================================================


@router.get("/personas/", response_model=PersonasListResponse)
async def list_personas():
    """List all 9 personas (brief info) and their locations.

    Returns high-level persona index with name, role, mandate, and file path.

    Touches φᵗ (temporal availability of persona specs).
    """
    loader = get_loader()
    personas = loader.load_personas()

    if not personas:
        raise HTTPException(status_code=404, detail="No personas found")

    return PersonasListResponse(personas=personas, count=len(personas))


@router.get("/personas/{persona_name}", response_model=PersonaResponse)
async def get_persona(persona_name: str):
    """Get full specification for a specific persona.

    Args:
        persona_name: Persona identifier (e.g., 'luminai', 'airth', 'arcadia', 'ely', 'companion', 'fusion')

    Returns persona spec including title, full content, metadata, and file path.

    Touches φᵗ (temporal access) and Φᴱ (contextual persona knowledge).
    """
    loader = get_loader()
    personas = loader.load_personas()

    persona_key = persona_name.lower()
    if persona_key not in personas:
        raise HTTPException(
            status_code=404, detail=f"Persona '{persona_name}' not found"
        )

    persona = personas[persona_key]
    if "error" in persona:
        raise HTTPException(status_code=500, detail=persona["error"])

    return PersonaResponse(
        name=persona_key,
        title=persona.get("title", ""),
        content=persona.get("content", ""),
        path=persona.get("path", ""),
        metadata=persona.get("metadata", {}),
    )


# ============================================================================
# GUIDES ENDPOINTS
# ============================================================================


@router.get("/guides/", response_model=GuidesListResponse)
async def list_guides():
    """List all deployment and reference guides.

    Available guides:
    - pull_and_build: Fresh clone and local setup
    - system_integration: System architecture and workflows
    - shareable_vs_internal_classification: File classification rules
    - gpt_deployment_ready: GPT Builder deployment steps
    - gpt_personas_attachment_decision: Which personas to attach to GPT
    - gpt_attachment_cheat_sheet: Quick reference for GPT uploads

    Touches ψʳ (structural cadence of deployment workflow).
    """
    loader = get_loader()
    guides = loader.load_guides()

    if not guides:
        raise HTTPException(status_code=404, detail="No guides found")

    return GuidesListResponse(guides=guides, count=len(guides))


@router.get("/guides/{guide_name}", response_model=GuideResponse)
async def get_guide(guide_name: str):
    """Get full content of a specific deployment guide.

    Args:
        guide_name: Guide identifier (e.g., 'pull_and_build', 'system_integration', 'gpt_deployment_ready')

    Returns complete guide including title, full content, and file path.

    Touches ψʳ (workflow structure) and Φᴱ (contextual deployment knowledge).
    """
    loader = get_loader()
    guides = loader.load_guides()

    guide_key = guide_name.lower().replace("-", "_")
    if guide_key not in guides:
        raise HTTPException(status_code=404, detail=f"Guide '{guide_name}' not found")

    guide = guides[guide_key]
    if "error" in guide:
        raise HTTPException(status_code=500, detail=guide["error"])

    return GuideResponse(
        name=guide_key,
        title=guide.get("title", ""),
        content=guide.get("content", ""),
        path=guide.get("path", ""),
    )


# ============================================================================
# CLASSIFICATION ENDPOINTS
# ============================================================================


@router.get("/classification/", response_model=ClassificationResponse)
async def get_classification():
    """Get shareable vs. internal file classification rules.

    Returns complete classification including:
    - 🟢 SHAREABLE categories (personas, docs, code, GPT guides, brand)
    - 🔴 INTERNAL-ONLY categories (secrets, .env, .venv, archives)
    - 🟡 CONDITIONAL categories (files needing sanitization)
    - Naming conventions and folder-level rules

    Touches ψʳ (structural integrity) and Φᴱ (security context).
    """
    loader = get_loader()
    classification = loader.load_classification()

    if "error" in classification:
        raise HTTPException(status_code=404, detail=classification["error"])

    return ClassificationResponse(
        title=classification.get("title", ""),
        content=classification.get("content", ""),
        path=classification.get("path", ""),
        categories=classification.get("categories", {}),
    )


# ============================================================================
# SYSTEM INFO ENDPOINTS
# ============================================================================


@router.get("/system/", response_model=SystemInfoResponse)
async def get_system_info():
    """Get system integration guide with architecture diagrams and workflows.

    Returns complete system integration guide including:
    - System architecture diagram
    - Typical workflows (fresh clone, GPT deployment, contributions)
    - Pre-push checklists
    - Troubleshooting guide
    - Next steps by role

    Touches φᵗ (temporal flow), ψʳ (system structure), and Φᴱ (coherence).
    """
    loader = get_loader()
    system_info = loader.load_system_info()

    if "error" in system_info:
        raise HTTPException(status_code=404, detail=system_info["error"])

    return SystemInfoResponse(
        title=system_info.get("title", ""),
        content=system_info.get("content", ""),
        path=system_info.get("path", ""),
    )


# ============================================================================
# UNIFIED KNOWLEDGE BASE ENDPOINT
# ============================================================================


@router.get("/knowledge/", response_model=KnowledgeBaseResponse)
async def get_all_knowledge():
    """Get complete unified knowledge base (all assets at once).

    Returns:
    - All 9 personas
    - All deployment guides
    - Classification rules
    - System integration info
    - Metadata (load time, asset counts, sync status)

    Perfect for:
    - Initializing client applications
    - Building comprehensive knowledge index
    - Verifying system coherence
    - Backing up or auditing knowledge state

    Touches all three TGCR variables: φᵗ (temporal availability),
    ψʳ (structural coherence), Φᴱ (full contextual potential).
    """
    loader = get_loader()
    knowledge = loader.load_all()

    return KnowledgeBaseResponse(
        personas=knowledge.get("personas", {}),
        guides=knowledge.get("guides", {}),
        classification=knowledge.get("classification", {}),
        system=knowledge.get("system", {}),
        metadata=knowledge.get("metadata", {}),
    )


# ============================================================================
# HEALTH CHECK
# ============================================================================


@router.get("/knowledge/health/")
async def knowledge_health():
    """Quick health check: verify all knowledge assets load successfully.

    Returns status and asset counts.

    Touches φᵗ (availability check).
    """
    loader = get_loader()
    knowledge = loader.load_all()

    return {
        "status": "healthy",
        "personas_loaded": len(knowledge.get("personas", {})),
        "guides_loaded": len(knowledge.get("guides", {})),
        "auto_synced": True,
        "last_sync": knowledge.get("metadata", {}).get("loaded_at"),
    }

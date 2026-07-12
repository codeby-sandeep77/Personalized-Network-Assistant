"""Wikipedia fact-checking API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/wikipedia", tags=["Wikipedia"])


@router.get("/health")
def wikipedia_health():
    """Health check for wikipedia module."""
    return {"status": "ok", "module": "wikipedia"}

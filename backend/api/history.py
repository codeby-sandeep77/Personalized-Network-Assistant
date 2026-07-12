"""History management API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/history", tags=["History"])


@router.get("/health")
def history_health():
    """Health check for history module."""
    return {"status": "ok", "module": "history"}

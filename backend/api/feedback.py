"""Feedback API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.get("/health")
def feedback_health():
    """Health check for feedback module."""
    return {"status": "ok", "module": "feedback"}

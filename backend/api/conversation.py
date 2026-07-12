"""Conversation generation API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/conversation", tags=["Conversation"])


@router.get("/health")
def conversation_health():
    """Health check for conversation module."""
    return {"status": "ok", "module": "conversation"}

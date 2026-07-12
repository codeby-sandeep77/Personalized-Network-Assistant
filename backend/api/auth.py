"""Authentication API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/health")
def auth_health():
    """Health check for auth module."""
    return {"status": "ok", "module": "auth"}

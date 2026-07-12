"""User management API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/health")
def users_health():
    """Health check for users module."""
    return {"status": "ok", "module": "users"}

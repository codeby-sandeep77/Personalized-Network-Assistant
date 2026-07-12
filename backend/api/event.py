"""Event and theme extraction API routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/health")
def events_health():
    """Health check for events module."""
    return {"status": "ok", "module": "events"}

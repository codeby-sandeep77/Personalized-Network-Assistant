"""Initial test suite for Epic 1."""

import pytest
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root_endpoint():
    """Root endpoint returns app info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "Personalized Networking Assistant"
    assert data["status"] == "running"


def test_health_check():
    """Health check endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.parametrize(
    "path,module",
    [
        ("/api/v1/auth/health", "auth"),
        ("/api/v1/users/health", "users"),
        ("/api/v1/events/health", "events"),
        ("/api/v1/history/health", "history"),
        ("/api/v1/feedback/health", "feedback"),
        ("/api/v1/wikipedia/health", "wikipedia"),
        ("/api/v1/conversation/health", "conversation"),
    ],
)
def test_module_health_endpoints(path, module):
    """Each API module exposes a health endpoint."""
    response = client.get(path)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["module"] == module

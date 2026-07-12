"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import auth, conversation, event, feedback, history, users, wikipedia
from backend.core.config import settings
from backend.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered networking assistant for event preparation",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(event.router, prefix="/api/v1")
app.include_router(history.router, prefix="/api/v1")
app.include_router(feedback.router, prefix="/api/v1")
app.include_router(wikipedia.router, prefix="/api/v1")
app.include_router(conversation.router, prefix="/api/v1")


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "running",
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

"""Health check endpoints."""

from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.db.session import check_database_connection
from app.core.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint.

    Returns application status and environment information.
    """
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "api_version": "v1",
    }


@router.get("/health/db")
async def health_check_database():
    """
    Database health check endpoint.

    Verifies database connectivity and returns connection status.
    """
    if not settings.DATABASE_URL:
        raise HTTPException(
            status_code=503,
            detail="Database not configured. Set DATABASE_URL environment variable.",
        )

    is_connected = check_database_connection()

    if not is_connected:
        raise HTTPException(
            status_code=503, detail="Database connection failed. Check configuration and network."
        )

    return {
        "status": "healthy",
        "database": "connected",
        "app_name": settings.APP_NAME,
    }

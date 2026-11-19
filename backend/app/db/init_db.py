"""Database initialization utilities."""

from app.db.base import Base
from app.db.session import engine, init_database
from app.core.logging import get_logger

logger = get_logger(__name__)


def create_tables() -> None:
    """Create all database tables. Used for initial setup or testing."""
    init_database()

    if engine is None:
        raise RuntimeError("Database engine not initialized")

    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")


def init_db() -> None:
    """
    Initialize database with default data if needed.
    This is where you would create initial users, settings, etc.
    """
    init_database()
    logger.info("Database initialization complete")

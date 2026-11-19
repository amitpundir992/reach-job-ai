"""Database session management."""

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

# Database engine (created lazily)
engine = None
SessionLocal = None


def init_database() -> None:
    """Initialize database engine and session factory."""
    global engine, SessionLocal

    if engine is not None:
        return

    if not settings.DATABASE_URL:
        logger.warning(
            "DATABASE_URL not configured. Database operations will fail until configured."
        )
        return

    try:
        # Create engine with appropriate settings
        engine = create_engine(
            settings.DATABASE_URL,
            echo=settings.DEBUG,
            pool_pre_ping=True,
            # Use NullPool for serverless databases like Neon
            poolclass=NullPool if "neon" in settings.DATABASE_URL.lower() else None,
        )

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        logger.info("Database engine initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize database engine: {e}")
        raise


def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session.

    Yields:
        SQLAlchemy Session instance

    Raises:
        RuntimeError: If database is not configured
    """
    if SessionLocal is None:
        raise RuntimeError(
            "Database not configured. Please set DATABASE_URL environment variable."
        )

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> bool:
    """
    Check if database connection is working.

    Returns:
        True if connection successful, False otherwise
    """
    if engine is None:
        init_database()

    if engine is None:
        return False

    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"Database connection check failed: {e}")
        return False

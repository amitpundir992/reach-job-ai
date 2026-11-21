"""Database base class and model registry."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass


# Import all models here for Alembic auto-generation
from app.models.user import RefreshToken, User, UserSettings  # noqa: F401, E402

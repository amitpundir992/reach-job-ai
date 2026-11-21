"""User repository for database operations."""

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.user import RefreshToken, User, UserSettings


class UserRepository:
    """Repository for user database operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def create(self, email: str, full_name: str, hashed_password: str) -> User:
        """Create a new user."""
        user = User(
            email=email,
            full_name=full_name,
            hashed_password=hashed_password,
            is_active=True,
            is_verified=False,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        # Create default settings for the user
        settings = UserSettings(user_id=user.id)
        self.db.add(settings)
        self.db.commit()

        return user

    def update(self, user: User) -> User:
        """Update user."""
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user


class RefreshTokenRepository:
    """Repository for refresh token database operations."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: uuid.UUID, token_hash: str, expires_at: datetime) -> RefreshToken:
        """Create a new refresh token."""
        refresh_token = RefreshToken(
            user_id=user_id,
            token_hash=token_hash,
            expires_at=expires_at,
        )
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token

    def get_by_token_hash(self, token_hash: str) -> RefreshToken | None:
        """Get refresh token by hash."""
        return self.db.query(RefreshToken).filter(RefreshToken.token_hash == token_hash).first()

    def revoke(self, refresh_token: RefreshToken) -> RefreshToken:
        """Revoke a refresh token."""
        refresh_token.revoked_at = datetime.now(timezone.utc)
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token

    def revoke_all_user_tokens(self, user_id: uuid.UUID) -> None:
        """Revoke all refresh tokens for a user."""
        tokens = (
            self.db.query(RefreshToken)
            .filter(RefreshToken.user_id == user_id, RefreshToken.revoked_at.is_(None))
            .all()
        )

        now = datetime.now(timezone.utc)
        for token in tokens:
            token.revoked_at = now
            self.db.add(token)

        self.db.commit()

    def cleanup_expired_tokens(self) -> int:
        """Delete expired tokens. Returns count of deleted tokens."""
        cutoff = datetime.now(timezone.utc)
        expired_tokens = self.db.query(RefreshToken).filter(RefreshToken.expires_at < cutoff).all()

        count = len(expired_tokens)
        for token in expired_tokens:
            self.db.delete(token)

        self.db.commit()
        return count


class UserSettingsRepository:
    """Repository for user settings database operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_user_id(self, user_id: uuid.UUID) -> UserSettings | None:
        """Get user settings by user ID."""
        return self.db.query(UserSettings).filter(UserSettings.user_id == user_id).first()

    def create(self, user_id: uuid.UUID, **kwargs) -> UserSettings:
        """Create user settings."""
        settings = UserSettings(user_id=user_id, **kwargs)
        self.db.add(settings)
        self.db.commit()
        self.db.refresh(settings)
        return settings

    def update(self, settings: UserSettings, **kwargs) -> UserSettings:
        """Update user settings."""
        for key, value in kwargs.items():
            if hasattr(settings, key):
                setattr(settings, key, value)

        settings.updated_at = datetime.now(timezone.utc)
        self.db.add(settings)
        self.db.commit()
        self.db.refresh(settings)
        return settings

"""Authentication service for business logic."""

import uuid
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    get_password_hash,
    hash_token,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import (
    RefreshTokenRepository,
    UserRepository,
)
from app.schemas.user import TokenResponse, UserCreate, UserLogin, UserResponse


class AuthService:
    """Service for authentication operations."""

    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.refresh_token_repo = RefreshTokenRepository(db)

    def register(self, user_data: UserCreate) -> UserResponse:
        """
        Register a new user.

        Args:
            user_data: User registration data

        Returns:
            Created user

        Raises:
            HTTPException: If user already exists
        """
        # Check if user already exists
        existing_user = self.user_repo.get_by_email(user_data.email)
        if existing_user:
            # Prevent user enumeration - use generic error message
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Registration failed. Please check your details and try again.",
            )

        # Hash password
        hashed_password = get_password_hash(user_data.password)

        # Create user
        user = self.user_repo.create(
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
        )

        return UserResponse.model_validate(user)

    def login(self, login_data: UserLogin) -> TokenResponse:
        """
        Authenticate user and return tokens.

        Args:
            login_data: User login credentials

        Returns:
            Access and refresh tokens

        Raises:
            HTTPException: If authentication fails
        """
        # Get user
        user = self.user_repo.get_by_email(login_data.email)

        # Prevent user enumeration - use generic error for all auth failures
        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if user is active
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive",
            )

        # Create tokens
        return self._create_tokens(user)

    def refresh(self, refresh_token: str) -> TokenResponse:
        """
        Refresh access token using refresh token.

        Args:
            refresh_token: Refresh token string

        Returns:
            New access and refresh tokens

        Raises:
            HTTPException: If refresh token is invalid
        """
        # Hash the provided token
        token_hash = hash_token(refresh_token)

        # Get refresh token from database
        db_token = self.refresh_token_repo.get_by_token_hash(token_hash)

        if not db_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if token is revoked
        if db_token.revoked_at is not None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has been revoked",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if token is expired
        if db_token.expires_at < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Get user
        user = self.user_repo.get_by_id(db_token.user_id)
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found or inactive",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Revoke old token (token rotation)
        self.refresh_token_repo.revoke(db_token)

        # Create new tokens
        return self._create_tokens(user)

    def logout(self, refresh_token: str) -> None:
        """
        Logout user by revoking refresh token.

        Args:
            refresh_token: Refresh token to revoke
        """
        token_hash = hash_token(refresh_token)
        db_token = self.refresh_token_repo.get_by_token_hash(token_hash)

        if db_token and db_token.revoked_at is None:
            self.refresh_token_repo.revoke(db_token)

    def logout_all(self, user_id: uuid.UUID) -> None:
        """
        Logout user from all devices by revoking all refresh tokens.

        Args:
            user_id: User ID
        """
        self.refresh_token_repo.revoke_all_user_tokens(user_id)

    def _create_tokens(self, user: User) -> TokenResponse:
        """
        Create access and refresh tokens for user.

        Args:
            user: User instance

        Returns:
            Token response with access and refresh tokens
        """
        # Create access token
        access_token_data = {
            "sub": str(user.id),
            "email": user.email,
        }
        access_token = create_access_token(access_token_data)

        # Create refresh token
        refresh_token_str = create_refresh_token()
        refresh_token_hash = hash_token(refresh_token_str)

        # Store refresh token in database
        expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        self.refresh_token_repo.create(
            user_id=user.id,
            token_hash=refresh_token_hash,
            expires_at=expires_at,
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token_str,
            token_type="bearer",
        )

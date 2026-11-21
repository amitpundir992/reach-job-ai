"""Authentication endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_active_user
from app.core.logging import get_logger
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import (
    RefreshTokenRequest,
    TokenResponse,
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.auth_service import AuthService

logger = get_logger(__name__)
router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_data: UserCreate,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Register a new user.

    Args:
        user_data: User registration data
        db: Database session

    Returns:
        Created user data
    """
    try:
        auth_service = AuthService(db)
        user = auth_service.register(user_data)
        logger.info(f"User registered successfully: {user.email}")
        return user
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Registration error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed",
        )


@router.post("/login", response_model=TokenResponse)
def login(
    login_data: UserLogin,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Login user and return access tokens.

    Args:
        login_data: User login credentials
        db: Database session

    Returns:
        Access and refresh tokens
    """
    try:
        auth_service = AuthService(db)
        tokens = auth_service.login(login_data)
        logger.info(f"User logged in successfully: {login_data.email}")
        return tokens
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed",
        )


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(
    refresh_data: RefreshTokenRequest,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Refresh access token using refresh token.

    Args:
        refresh_data: Refresh token
        db: Database session

    Returns:
        New access and refresh tokens
    """
    try:
        auth_service = AuthService(db)
        tokens = auth_service.refresh(refresh_data.refresh_token)
        logger.info("Token refreshed successfully")
        return tokens
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Token refresh error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token refresh failed",
        )


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    refresh_data: RefreshTokenRequest,
    db: Annotated[Session, Depends(get_db)],
):
    """
    Logout user by revoking refresh token.

    Args:
        refresh_data: Refresh token to revoke
        db: Database session
    """
    try:
        auth_service = AuthService(db)
        auth_service.logout(refresh_data.refresh_token)
        logger.info("User logged out successfully")
        return None
    except Exception as e:
        logger.error(f"Logout error: {e}", exc_info=True)
        # Don't raise error on logout - just log it
        return None


@router.get("/me", response_model=UserResponse)
def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """
    Get current authenticated user information.

    Args:
        current_user: Current authenticated user

    Returns:
        Current user data
    """
    return UserResponse.model_validate(current_user)

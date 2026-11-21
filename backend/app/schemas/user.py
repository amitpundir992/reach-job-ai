"""User schemas for request/response validation."""

import re
import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)


class UserCreate(UserBase):
    """Schema for user registration."""

    password: str = Field(..., min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Validate password strength.

        Requirements:
        - At least 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
        """
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")

        return v

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v: str) -> str:
        """Validate full name is not empty or whitespace."""
        if not v.strip():
            raise ValueError("Full name cannot be empty")
        return v.strip()


class UserLogin(BaseModel):
    """Schema for user login."""

    email: EmailStr
    password: str = Field(..., min_length=1)


class UserResponse(UserBase):
    """Schema for user response."""

    id: uuid.UUID
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    """Schema for token response."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    """Schema for refresh token request."""

    refresh_token: str = Field(..., min_length=1)


class UserSettingsBase(BaseModel):
    """Base user settings schema."""

    preferred_roles: str | None = None
    preferred_locations: str | None = None
    preferred_technologies: str | None = None


class UserSettingsCreate(UserSettingsBase):
    """Schema for creating user settings."""

    pass


class UserSettingsUpdate(UserSettingsBase):
    """Schema for updating user settings."""

    pass


class UserSettingsResponse(UserSettingsBase):
    """Schema for user settings response."""

    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

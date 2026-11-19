"""Application configuration using Pydantic Settings."""

import json
from typing import List
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_NAME: str = Field(default="ReachJobAI")
    APP_ENV: str = Field(default="development")
    DEBUG: bool = Field(default=True)
    API_V1_PREFIX: str = Field(default="/api/v1")

    # Database
    DATABASE_URL: str | None = Field(default=None)

    # Security
    JWT_SECRET_KEY: str = Field(default="insecure-development-secret-change-in-production")
    JWT_ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)

    # AI Integration
    GEMINI_API_KEY: str | None = Field(default=None)

    # CORS
    FRONTEND_URL: str = Field(default="http://localhost:5173")
    BACKEND_CORS_ORIGINS: List[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        """Parse CORS origins from JSON string or list."""
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [origin.strip() for origin in v.split(",")]
        return v

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.APP_ENV.lower() == "production"

    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.APP_ENV.lower() == "development"


# Global settings instance
settings = Settings()

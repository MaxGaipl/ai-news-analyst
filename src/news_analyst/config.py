"""
Minimal configuration for AI News Analyst.

Following YAGNI principles - only basic settings needed for project setup.
More configuration will be added as features are implemented.
"""

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Basic application settings for project setup."""

    # Application metadata
    app_name: str = Field(default="AI News Analyst", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    environment: str = Field(default="development", description="Environment")
    debug: bool = Field(default=True, description="Enable debug mode")

    # Minimal database config (just what's needed for setup)
    database_url: str = Field(
        default="sqlite+aiosqlite:///./data/news_analyst.db",
        description="Database connection URL",
    )

    # Pydantic settings configuration
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    @property
    def project_root(self) -> Path:
        """Get the project root directory."""
        return Path(__file__).parent.parent.parent

    @property
    def data_dir(self) -> Path:
        """Get the data directory."""
        return self.project_root / "data"

    @property
    def logs_dir(self) -> Path:
        """Get the logs directory."""
        return self.project_root / "logs"

    def ensure_directories(self) -> None:
        """Ensure required directories exist."""
        directories = [
            self.data_dir / "raw",
            self.data_dir / "processed",
            self.data_dir / "cache",
            self.logs_dir,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings()

# Ensure directories exist on import
settings.ensure_directories()

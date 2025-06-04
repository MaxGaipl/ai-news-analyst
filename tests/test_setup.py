"""
Test basic project setup and imports.

This test verifies that Issue #1 setup is working correctly.
"""

import pytest


def test_can_import_main_package():
    """Test that we can import the main package."""
    from news_analyst import settings

    assert settings.app_name == "AI News Analyst"
    assert settings.app_version == "0.1.0"
    assert settings.environment == "development"


def test_settings_configuration():
    """Test that settings are properly configured."""
    from news_analyst.config import settings

    # Test basic properties
    assert settings.debug is True
    assert settings.database_url.startswith("sqlite+aiosqlite://")

    # Test directory properties
    assert settings.project_root.exists()
    assert settings.data_dir.exists()
    assert settings.logs_dir.exists()


def test_core_dependencies_can_be_imported():
    """Test that core dependencies are available."""

    # Test Crawl4AI
    import crawl4ai
    from crawl4ai import AsyncWebCrawler, BrowserConfig

    # Test Pydantic AI
    import pydantic_ai
    from pydantic_ai import Agent

    # Test FastAPI
    import fastapi
    from fastapi import FastAPI

    # Test SQLAlchemy
    import sqlalchemy
    from sqlalchemy.ext.asyncio import AsyncSession

    # Test Pydantic Settings
    from pydantic_settings import BaseSettings

    # If we get here, all imports worked
    assert True


def test_project_directories_exist():
    """Test that all required project directories exist."""
    from news_analyst.config import settings

    # Test main data directories
    assert (settings.data_dir / "raw").exists()
    assert (settings.data_dir / "processed").exists()
    assert (settings.data_dir / "cache").exists()
    assert settings.logs_dir.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

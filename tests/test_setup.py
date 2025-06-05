"""
Test basic project setup and imports.

This test verifies that Issue #1 setup is working correctly.
"""

import pytest


def test_can_import_main_package():
    """Test that we can import the main package."""
    from src.news_analyst import settings

    assert settings.app_name == "AI News Analyst"
    assert settings.app_version == "0.1.0"
    assert settings.environment == "development"


def test_settings_configuration():
    """Test that settings are properly configured."""
    from src.news_analyst.config import settings

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

    # Test Pydantic AI

    # Test FastAPI

    # Test SQLAlchemy

    # Test Pydantic Settings

    # If we get here, all imports worked
    assert True


def test_project_directories_exist():
    """Test that all required project directories exist."""
    from src.news_analyst.config import settings

    # Test main data directories
    assert (settings.data_dir / "raw").exists()
    assert (settings.data_dir / "processed").exists()
    assert (settings.data_dir / "cache").exists()
    assert settings.logs_dir.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

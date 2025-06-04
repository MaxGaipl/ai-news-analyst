#!/usr/bin/env python3
"""
Issue #1 Verification Script

This script verifies that all requirements of Issue #1 have been completed:
- Project structure is set up correctly
- Core dependencies are installed and importable
- Configuration system is working
- All directories exist
"""

import sys
from pathlib import Path

# Add src to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))


def check_project_structure():
    """Verify project structure exists."""
    print("🔍 Checking project structure...")

    required_dirs = [
        "src/news_analyst",
        "src/news_analyst/models",
        "src/news_analyst/scrapers",
        "src/news_analyst/agents",
        "src/news_analyst/database",
        "src/news_analyst/services",
        "src/news_analyst/api",
        "tests/unit",
        "tests/integration",
        "tests/e2e",
        "scripts",
        "data/raw",
        "data/processed",
        "data/cache",
        "logs",
    ]

    missing_dirs = []
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if not full_path.exists():
            missing_dirs.append(dir_path)

    if missing_dirs:
        print(f"❌ Missing directories: {missing_dirs}")
        return False
    else:
        print("✅ All required directories exist")
        return True


def check_core_files():
    """Verify core files exist."""
    print("🔍 Checking core files...")

    required_files = [
        "pyproject.toml",
        "README.md",
        ".gitignore",
        ".env",
        "src/news_analyst/__init__.py",
        "src/news_analyst/config.py",
    ]

    missing_files = []
    for file_path in required_files:
        full_path = project_root / file_path
        if not full_path.exists():
            missing_files.append(file_path)

    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files exist")
        return True


def check_dependencies():
    """Verify core dependencies can be imported."""
    print("🔍 Checking core dependencies...")

    dependencies = [
        ("crawl4ai", "crawl4ai"),
        ("pydantic_ai", "pydantic_ai"),
        ("fastapi", "fastapi"),
        ("sqlalchemy", "sqlalchemy"),
        ("pydantic_settings", "pydantic_settings"),
        ("alembic", "alembic"),
        ("uvicorn", "uvicorn"),
        ("pytest", "pytest"),
    ]

    failed_imports = []
    for name, module in dependencies:
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError as e:
            print(f"  ❌ {name}: {e}")
            failed_imports.append(name)

    if failed_imports:
        print(f"❌ Failed to import: {failed_imports}")
        return False
    else:
        print("✅ All dependencies importable")
        return True


def check_package_imports():
    """Verify our package can be imported."""
    print("🔍 Checking package imports...")

    try:
        from news_analyst import settings

        print(f"  ✅ Main package import: {settings.app_name} v{settings.app_version}")

        from news_analyst.config import Settings

        print(f"  ✅ Config import: {Settings.__name__}")

        return True
    except Exception as e:
        print(f"❌ Package import failed: {e}")
        return False


def check_configuration():
    """Verify configuration system works."""
    print("🔍 Checking configuration...")

    try:
        from news_analyst.config import settings

        # Check basic settings
        assert settings.app_name == "AI News Analyst"
        assert settings.app_version == "0.1.0"
        assert settings.environment == "development"
        assert settings.debug is True

        # Check paths
        assert settings.project_root.exists()
        assert settings.data_dir.exists()
        assert settings.logs_dir.exists()

        print("✅ Configuration system working")
        return True
    except Exception as e:
        print(f"❌ Configuration check failed: {e}")
        return False


def main():
    """Run all verification checks."""
    print("🚀 Verifying Issue #1 completion...\n")

    checks = [
        check_project_structure,
        check_core_files,
        check_dependencies,
        check_package_imports,
        check_configuration,
    ]

    results = []
    for check in checks:
        result = check()
        results.append(result)
        print()

    if all(results):
        print("🎉 Issue #1 COMPLETED! All requirements satisfied.")
        print("\n✅ Summary:")
        print("  - Project structure created")
        print("  - Core dependencies installed")
        print("  - Configuration system working")
        print("  - Package imports functional")
        print("  - Ready for Issue #2!")
        return 0
    else:
        print("❌ Issue #1 NOT COMPLETE. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

"""
AI News Analyst & Fact Checker

A modern Python application that combines intelligent web scraping with LLM-powered
fact-checking and analysis of news articles.

This package provides:
- Intelligent web scraping with Crawl4AI
- LLM-powered news analysis with Pydantic AI
- Structured data models with Pydantic
- Async database operations with SQLAlchemy
- REST API with FastAPI
"""

__version__ = "0.1.0"
__author__ = "Max Gaipl"

# Basic configuration for project setup
from .config import settings

__all__ = [
    "settings",
]

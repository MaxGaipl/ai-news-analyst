# Pydantic Data Models

"""
News Analyst Data Models

This module contains all Pydantic data models used throughout the application
for representing news articles, analysis results, and related entities.
"""

from .base import BaseNewsModel, TimestampMixin, UUIDMixin
from .article import Article
from .news_source import NewsSource, BiasRating, CredibilityRating
from .fact_check import FactCheckClaim, VerificationStatus
from .analysis import AnalysisResult, Sentiment, SentimentLabel, BiasLabel, CredibilityLabel

__all__ = [
    # Base models and mixins
    "BaseNewsModel",
    "TimestampMixin",
    "UUIDMixin",
    # Core models
    "Article",
    "NewsSource",
    "FactCheckClaim",
    "AnalysisResult",
    "Sentiment",
    # Enums
    "BiasRating",
    "CredibilityRating",
    "VerificationStatus",
    "SentimentLabel",
    "BiasLabel",
    "CredibilityLabel",
]

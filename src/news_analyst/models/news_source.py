"""
News source model for representing media outlets.
"""

from enum import StrEnum
from typing import Optional, List
from uuid import UUID

from pydantic import Field, HttpUrl, field_validator

from .base import BaseNewsModel, UUIDMixin, TimestampMixin


class BiasRating(StrEnum):
    """Political bias rating for news sources."""

    LEFT = "left"
    LEFT_CENTER = "left_center"
    CENTER = "center"
    RIGHT_CENTER = "right_center"
    RIGHT = "right"
    UNKNOWN = "unknown"


class CredibilityRating(StrEnum):
    """Credibility rating for news sources."""

    VERY_HIGH = "very_high"
    HIGH = "high"
    MIXED = "mixed"
    LOW = "low"
    VERY_LOW = "very_low"
    UNKNOWN = "unknown"


class NewsSource(BaseNewsModel, UUIDMixin, TimestampMixin):
    """
    Represents a news media source/outlet.

    This model stores information about news sources including
    their credibility ratings, bias assessments, and metadata.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Name of the news source (e.g., 'BBC News', 'Reuters')",
    )

    url: HttpUrl = Field(..., description="Main website URL of the news source")

    bias_rating: BiasRating = Field(
        default=BiasRating.UNKNOWN,
        description="Political bias assessment of the source",
    )

    credibility_rating: CredibilityRating = Field(
        default=CredibilityRating.UNKNOWN,
        description="Credibility/reliability rating of the source",
    )

    active: bool = Field(
        default=True, description="Whether this source is actively being scraped"
    )

    country: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=3,
        description="Country code where the source is based (ISO 3166-1)",
    )

    language: str = Field(
        default="en",
        min_length=2,
        max_length=5,
        description="Primary language of the source (ISO 639-1)",
    )

    description: Optional[str] = Field(
        default=None, max_length=500, description="Brief description of the news source"
    )

    rss_feeds: List[HttpUrl] = Field(
        default_factory=list, description="List of RSS feed URLs for this source"
    )

    scraping_selectors: Optional[dict] = Field(
        default=None, description="CSS selectors for scraping this source"
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate and normalize source name."""
        # Strip whitespace and ensure proper capitalization
        normalized = v.strip()
        if not normalized:
            raise ValueError("Source name cannot be empty")
        return normalized

    @field_validator("rss_feeds")
    @classmethod
    def validate_rss_feeds(cls, v: List[HttpUrl]) -> List[HttpUrl]:
        """Validate RSS feeds and remove duplicates."""
        if not v:
            return []

        # Remove duplicates while preserving order
        unique_feeds = []
        seen = set()
        for feed in v:
            feed_str = str(feed)
            if feed_str not in seen:
                unique_feeds.append(feed)
                seen.add(feed_str)

        return unique_feeds

    def is_reliable(self) -> bool:
        """Check if the source has high credibility."""
        return self.credibility_rating in {
            CredibilityRating.VERY_HIGH,
            CredibilityRating.HIGH,
        }

    def is_neutral(self) -> bool:
        """Check if the source has neutral political bias."""
        return self.bias_rating == BiasRating.CENTER

"""
Article model for representing news articles.
"""

from datetime import datetime
from typing import Optional, List

from pydantic import Field, HttpUrl, field_validator

from .base import BaseNewsModel, UUIDMixin, TimestampMixin


class Article(BaseNewsModel, UUIDMixin, TimestampMixin):
    """
    Represents a news article with all its metadata and content.

    This model stores the core information about a news article including
    its content, source information, and metadata related to when it was
    published and scraped.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="The headline/title of the article",
    )

    content: str = Field(
        ..., min_length=10, description="Full text content of the article"
    )

    url: HttpUrl = Field(..., description="Original URL where the article was found")

    source: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Name of the news source (e.g., 'BBC', 'Reuters')",
    )

    published_at: Optional[datetime] = Field(
        default=None, description="When the article was originally published"
    )

    scraped_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When the article was scraped from the web",
    )

    author: Optional[str] = Field(
        default=None, max_length=200, description="Author(s) of the article"
    )

    tags: List[str] = Field(
        default_factory=list,
        description="Tags or categories associated with the article",
    )

    summary: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Brief summary of the article content",
    )

    language: str = Field(
        default="en",
        min_length=2,
        max_length=5,
        description="Language code of the article (ISO 639-1)",
    )

    word_count: Optional[int] = Field(
        default=None, ge=0, description="Number of words in the article content"
    )

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: List[str]) -> List[str]:
        """Validate that tags are non-empty strings and remove duplicates."""
        if not v:
            return []

        # Filter out empty tags and strip whitespace
        cleaned_tags = [tag.strip() for tag in v if tag and tag.strip()]

        # Remove duplicates while preserving order
        unique_tags = []
        seen = set()
        for tag in cleaned_tags:
            tag_lower = tag.lower()
            if tag_lower not in seen:
                unique_tags.append(tag)
                seen.add(tag_lower)

        return unique_tags

    @field_validator("content")
    @classmethod
    def calculate_word_count(cls, v: str) -> str:
        """Calculate and set word count when content is set."""
        return v

    def model_post_init(self, __context) -> None:
        """Post-initialization to calculate derived fields."""
        if self.content and self.word_count is None:
            # Simple word count calculation
            self.word_count = len(self.content.split())

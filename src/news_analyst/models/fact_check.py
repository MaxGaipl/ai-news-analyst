"""
Fact checking claim model.
"""

from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import Field, HttpUrl, field_validator

from .base import BaseNewsModel, UUIDMixin, TimestampMixin


class VerificationStatus(str, Enum):
    """Status of fact check verification."""

    TRUE = "true"
    FALSE = "false"
    PARTIALLY_TRUE = "partially_true"
    MISLEADING = "misleading"
    UNVERIFIED = "unverified"
    DISPUTED = "disputed"


class FactCheckClaim(BaseNewsModel, UUIDMixin, TimestampMixin):
    """
    Represents a fact-checkable claim extracted from an article.

    This model stores individual claims that can be fact-checked,
    along with their verification status and supporting sources.
    """

    claim_text: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="The actual claim text that needs verification",
    )

    verification_status: VerificationStatus = Field(
        default=VerificationStatus.UNVERIFIED,
        description="Current verification status of the claim",
    )

    sources: List[HttpUrl] = Field(
        default_factory=list,
        description="URLs of sources that support or refute this claim",
    )

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score for the verification (0.0 to 1.0)",
    )

    context: Optional[str] = Field(
        default=None, max_length=500, description="Additional context around the claim"
    )

    verification_notes: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="Notes about the verification process",
    )

    @field_validator("sources")
    @classmethod
    def validate_sources(cls, v: List[HttpUrl]) -> List[HttpUrl]:
        """Validate sources and remove duplicates."""
        if not v:
            return []

        # Remove duplicates while preserving order
        unique_sources = []
        seen = set()
        for source in v:
            source_str = str(source)
            if source_str not in seen:
                unique_sources.append(source)
                seen.add(source_str)

        return unique_sources

    def is_verified(self) -> bool:
        """Check if the claim has been verified (any status except unverified)."""
        return self.verification_status != VerificationStatus.UNVERIFIED

    def is_credible(self) -> bool:
        """Check if the claim is considered credible (true or partially true)."""
        return self.verification_status in {
            VerificationStatus.TRUE,
            VerificationStatus.PARTIALLY_TRUE,
        }

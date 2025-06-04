"""
Analysis result model for storing article analysis data.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import Field, field_validator

from .base import BaseNewsModel, UUIDMixin, TimestampMixin
from .fact_check import FactCheckClaim


class SentimentLabel(str, Enum):
    """Sentiment analysis labels."""

    VERY_POSITIVE = "very_positive"
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    VERY_NEGATIVE = "very_negative"


class Sentiment(BaseNewsModel):
    """Sentiment analysis result."""

    label: SentimentLabel = Field(..., description="Sentiment classification label")

    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score for sentiment prediction (0.0 to 1.0)",
    )

    scores: Optional[dict] = Field(
        default=None, description="Raw sentiment scores for all classes"
    )


class AnalysisResult(BaseNewsModel, UUIDMixin, TimestampMixin):
    """
    Represents the complete analysis result for a news article.

    This model aggregates all analysis outputs including bias detection,
    credibility scoring, sentiment analysis, and fact-checking results.
    """

    article_id: UUID = Field(..., description="Reference to the analyzed article")

    bias_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Political bias score (0.0 = left bias, 0.5 = neutral, 1.0 = right bias)",
    )

    credibility_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Overall credibility score (0.0 = not credible, 1.0 = highly credible)",
    )

    sentiment: Sentiment = Field(..., description="Sentiment analysis result")

    fact_check_claims: List[FactCheckClaim] = Field(
        default_factory=list,
        description="List of fact-checkable claims found in the article",
    )

    summary: Optional[str] = Field(
        default=None,
        max_length=1000,
        description="AI-generated summary of the analysis findings",
    )

    analyzed_at: datetime = Field(
        default_factory=datetime.utcnow, description="When the analysis was performed"
    )

    analysis_version: str = Field(
        default="1.0", description="Version of the analysis algorithm used"
    )

    processing_time_ms: Optional[int] = Field(
        default=None,
        ge=0,
        description="Time taken to complete the analysis in milliseconds",
    )

    confidence_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Overall confidence in the analysis results",
    )

    @field_validator("fact_check_claims")
    @classmethod
    def validate_claims(cls, v: List[FactCheckClaim]) -> List[FactCheckClaim]:
        """Validate fact check claims."""
        return v if v else []

    @field_validator("bias_score", "credibility_score")
    @classmethod
    def validate_scores(cls, v: float) -> float:
        """Ensure scores are within valid range."""
        return max(0.0, min(1.0, v))

    def get_bias_label(self) -> str:
        """Get human-readable bias label based on score."""
        if self.bias_score < 0.3:
            return "Left Bias"
        elif self.bias_score < 0.4:
            return "Left-Center"
        elif self.bias_score < 0.6:
            return "Center/Neutral"
        elif self.bias_score < 0.7:
            return "Right-Center"
        else:
            return "Right Bias"

    def get_credibility_label(self) -> str:
        """Get human-readable credibility label based on score."""
        if self.credibility_score >= 0.8:
            return "Very High"
        elif self.credibility_score >= 0.6:
            return "High"
        elif self.credibility_score >= 0.4:
            return "Mixed"
        elif self.credibility_score >= 0.2:
            return "Low"
        else:
            return "Very Low"

    def has_verified_claims(self) -> bool:
        """Check if any claims have been fact-checked."""
        return any(claim.is_verified() for claim in self.fact_check_claims)

    def get_credible_claims_ratio(self) -> float:
        """Get ratio of credible to total verified claims."""
        verified_claims = [
            claim for claim in self.fact_check_claims if claim.is_verified()
        ]
        if not verified_claims:
            return 0.0

        credible_claims = [claim for claim in verified_claims if claim.is_credible()]
        return len(credible_claims) / len(verified_claims)

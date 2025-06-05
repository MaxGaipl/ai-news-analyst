"""
Tests for Pydantic data models.
"""

import pytest
from datetime import datetime
from uuid import UUID

from src.news_analyst.models import (
    Article,
    NewsSource,
    FactCheckClaim,
    AnalysisResult,
    Sentiment,
    BiasRating,
    CredibilityRating,
    VerificationStatus,
    SentimentLabel,
    BiasLabel,
    CredibilityLabel,
)


class TestArticle:
    """Test the Article model."""

    def test_article_creation(self):
        """Test creating a basic article."""
        article = Article(
            title="Test Article",
            content="This is a test article with some content to analyze.",
            url="https://example.com/article",
            source="Test Source",
        )

        assert article.title == "Test Article"
        assert article.source == "Test Source"
        assert isinstance(article.id, UUID)
        assert isinstance(article.created_at, datetime)
        assert article.word_count == 10  # Should auto-calculate

    def test_article_tags_validation(self):
        """Test tag validation and deduplication."""
        article = Article(
            title="Test Article",
            content="Test content for validation.",
            url="https://example.com/article",
            source="Test Source",
            tags=["politics", "POLITICS", "news", "", "news", "  world  "],
        )

        # Should remove duplicates and empty tags, preserve case for first occurrence
        expected_tags = ["politics", "news", "world"]
        assert article.tags == expected_tags


class TestNewsSource:
    """Test the NewsSource model."""

    def test_news_source_creation(self):
        """Test creating a news source."""
        source = NewsSource(
            name="BBC News",
            url="https://www.bbc.com/news",
            bias_rating=BiasRating.CENTER,
            credibility_rating=CredibilityRating.VERY_HIGH,
        )

        assert source.name == "BBC News"
        assert source.bias_rating == BiasRating.CENTER
        assert source.credibility_rating == CredibilityRating.VERY_HIGH
        assert source.is_reliable() is True
        assert source.is_neutral() is True

    def test_rss_feeds_deduplication(self):
        """Test RSS feeds deduplication."""
        source = NewsSource(
            name="Test Source",
            url="https://example.com",
            rss_feeds=[
                "https://example.com/rss",
                "https://example.com/feed",
                "https://example.com/rss",  # Duplicate
            ],
        )

        assert len(source.rss_feeds) == 2
        assert str(source.rss_feeds[0]) == "https://example.com/rss"
        assert str(source.rss_feeds[1]) == "https://example.com/feed"


class TestFactCheckClaim:
    """Test the FactCheckClaim model."""

    def test_fact_check_claim_creation(self):
        """Test creating a fact check claim."""
        claim = FactCheckClaim(
            claim_text="The president made this statement yesterday.",
            verification_status=VerificationStatus.TRUE,
            confidence=0.85,
        )

        assert claim.verification_status == VerificationStatus.TRUE
        assert claim.confidence == 0.85
        assert claim.is_verified() is True
        assert claim.is_credible() is True

    def test_unverified_claim(self):
        """Test unverified claim status."""
        claim = FactCheckClaim(claim_text="This is an unverified claim.")

        assert claim.verification_status == VerificationStatus.UNVERIFIED
        assert claim.is_verified() is False
        assert claim.is_credible() is False


class TestAnalysisResult:
    """Test the AnalysisResult model."""

    def test_analysis_result_creation(self):
        """Test creating an analysis result."""
        # Create article first
        article = Article(
            title="Test Article",
            content="Test content for analysis.",
            url="https://example.com/article",
            source="Test Source",
        )

        sentiment = Sentiment(label=SentimentLabel.NEUTRAL, confidence=0.75)

        result = AnalysisResult(
            article_id=article.id,
            bias_score=0.5,
            credibility_score=0.8,
            sentiment=sentiment,
        )

        assert result.article_id == article.id
        assert result.bias_score == 0.5
        assert result.credibility_score == 0.8
        assert result.get_bias_label() == BiasLabel.CENTER_NEUTRAL
        assert result.get_credibility_label() == CredibilityLabel.VERY_HIGH

    def test_analysis_with_claims(self):
        """Test analysis result with fact check claims."""
        article = Article(
            title="Test Article",
            content="Test content for analysis.",
            url="https://example.com/article",
            source="Test Source",
        )

        claims = [
            FactCheckClaim(
                claim_text="Verified claim",
                verification_status=VerificationStatus.TRUE,
                confidence=0.9,
            ),
            FactCheckClaim(
                claim_text="False claim",
                verification_status=VerificationStatus.FALSE,
                confidence=0.8,
            ),
        ]

        sentiment = Sentiment(label=SentimentLabel.POSITIVE, confidence=0.85)

        result = AnalysisResult(
            article_id=article.id,
            bias_score=0.3,
            credibility_score=0.6,
            sentiment=sentiment,
            fact_check_claims=claims,
        )

        assert result.has_verified_claims() is True
        assert result.get_credible_claims_ratio() == 0.5  # 1 out of 2 claims credible


class TestSentiment:
    """Test the Sentiment model."""

    def test_sentiment_creation(self):
        """Test creating a sentiment object."""
        sentiment = Sentiment(
            label=SentimentLabel.POSITIVE,
            confidence=0.85,
            scores={"positive": 0.85, "negative": 0.15},
        )

        assert sentiment.label == SentimentLabel.POSITIVE
        assert sentiment.confidence == 0.85
        assert sentiment.scores["positive"] == 0.85

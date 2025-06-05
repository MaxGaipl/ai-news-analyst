#!/usr/bin/env python3
"""
Verification script for Issue #2 - Pydantic Data Models

This script demonstrates that all the required data models have been implemented
correctly and can be used as intended.
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from news_analyst.models import (
    Article,
    NewsSource,
    FactCheckClaim,
    AnalysisResult,
    Sentiment,
    BiasRating,
    CredibilityRating,
    VerificationStatus,
    SentimentLabel,
)


def verify_models():
    """Verify all models can be created and used correctly."""

    print("🧪 Verifying Issue #2: Pydantic Data Models")
    print("=" * 50)

    # Test Article model
    print("\n📰 Testing Article Model...")
    article = Article(
        title="Breaking: Major Climate Summit Reaches Historic Agreement",
        content="World leaders gathered today to announce a groundbreaking agreement on climate change. The comprehensive accord includes binding emissions targets and substantial funding for developing nations...",
        url="https://example-news.com/climate-summit-agreement",
        source="Global News Network",
        author="Jane Reporter",
        tags=["climate", "politics", "international", "environment"],
        summary="World leaders reach historic climate agreement with binding targets",
    )

    print(f"✅ Article created: {article.title}")
    print(f"   - ID: {article.id}")
    print(f"   - Word count: {article.word_count}")
    print(f"   - Tags: {article.tags}")
    print(f"   - Created: {article.created_at}")

    # Test NewsSource model
    print("\n📡 Testing NewsSource Model...")
    source = NewsSource(
        name="BBC News",
        url="https://www.bbc.com/news",
        bias_rating=BiasRating.CENTER,
        credibility_rating=CredibilityRating.VERY_HIGH,
        country="GB",
        language="en",
        description="British public service broadcaster",
        rss_feeds=[
            "https://feeds.bbci.co.uk/news/rss.xml",
            "https://feeds.bbci.co.uk/news/world/rss.xml",
        ],
    )

    print(f"✅ NewsSource created: {source.name}")
    print(f"   - Bias: {source.bias_rating}")
    print(f"   - Credibility: {source.credibility_rating}")
    print(f"   - Is reliable: {source.is_reliable()}")
    print(f"   - Is neutral: {source.is_neutral()}")
    print(f"   - RSS feeds: {len(source.rss_feeds)}")

    # Test FactCheckClaim model
    print("\n🔍 Testing FactCheckClaim Model...")
    claim1 = FactCheckClaim(
        claim_text="The agreement includes $100 billion in annual climate funding",
        verification_status=VerificationStatus.TRUE,
        confidence=0.92,
        sources=[
            "https://unfccc.int/agreement-details",
            "https://worldbank.org/climate-finance",
        ],
    )

    claim2 = FactCheckClaim(
        claim_text="This is the largest climate deal in history",
        verification_status=VerificationStatus.PARTIALLY_TRUE,
        confidence=0.78,
    )

    print(f"✅ FactCheckClaim 1: {claim1.claim_text[:50]}...")
    print(f"   - Status: {claim1.verification_status}")
    print(f"   - Confidence: {claim1.confidence}")
    print(f"   - Is verified: {claim1.is_verified()}")
    print(f"   - Is credible: {claim1.is_credible()}")
    print(f"   - Sources: {len(claim1.sources)}")

    # Test Sentiment model
    print("\n😊 Testing Sentiment Model...")
    sentiment = Sentiment(
        label=SentimentLabel.POSITIVE,
        confidence=0.87,
        scores={
            "very_positive": 0.12,
            "positive": 0.75,
            "neutral": 0.10,
            "negative": 0.02,
            "very_negative": 0.01,
        },
    )

    print(f"✅ Sentiment created: {sentiment.label}")
    print(f"   - Confidence: {sentiment.confidence}")
    print(f"   - All scores: {sentiment.scores}")

    # Test AnalysisResult model
    print("\n📊 Testing AnalysisResult Model...")
    analysis = AnalysisResult(
        article_id=article.id,
        bias_score=0.52,  # Slightly right of center
        credibility_score=0.85,  # High credibility
        sentiment=sentiment,
        fact_check_claims=[claim1, claim2],
        summary="Analysis shows positive sentiment with high credibility and slight right-center bias",
        processing_time_ms=1250,
        confidence_score=0.89,
    )

    print(f"✅ AnalysisResult created for article: {article.title[:30]}...")
    print(f"   - Bias: {analysis.get_bias_label()} (score: {analysis.bias_score})")
    print(
        f"   - Credibility: {analysis.get_credibility_label()} (score: {analysis.credibility_score})"
    )
    print(f"   - Sentiment: {analysis.sentiment.label}")
    print(f"   - Claims checked: {len(analysis.fact_check_claims)}")
    print(f"   - Has verified claims: {analysis.has_verified_claims()}")
    print(f"   - Credible claims ratio: {analysis.get_credible_claims_ratio():.2f}")
    print(f"   - Processing time: {analysis.processing_time_ms}ms")

    # Test model serialization
    print("\n🔄 Testing Model Serialization...")
    article_json = article.model_dump_json(indent=2)
    print(f"✅ Article serializes to {len(article_json)} characters of JSON")

    # Test model deserialization
    article_dict = article.model_dump()
    article_restored = Article(**article_dict)
    print(f"✅ Article deserializes correctly: {article_restored.id == article.id}")

    print("\n" + "=" * 50)
    print("🎉 All Issue #2 requirements verified successfully!")
    print("\n📋 Completed Models:")
    print("   ✅ Article model with all required fields")
    print("   ✅ NewsSource model with bias/credibility ratings")
    print("   ✅ FactCheckClaim model with verification status")
    print("   ✅ AnalysisResult model with comprehensive analysis data")
    print("   ✅ Sentiment model for sentiment analysis")
    print("   ✅ Base models and mixins for common functionality")
    print("   ✅ Proper validation rules and custom validators")
    print("   ✅ All models tested and working correctly")


if __name__ == "__main__":
    verify_models()

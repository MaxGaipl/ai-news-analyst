"""
Base models and mixins for common functionality.
"""

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict


class TimestampMixin(BaseModel):
    """Mixin for models that need timestamp fields."""

    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="When the record was created"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="When the record was last updated"
    )


class UUIDMixin(BaseModel):
    """Mixin for models that use UUID as primary key."""

    id: UUID = Field(default_factory=uuid4, description="Unique identifier")


class BaseNewsModel(BaseModel):
    """Base model for all news analyst entities."""

    model_config = ConfigDict(
        # Enable validation on assignment
        validate_assignment=True,
        # Use enum values instead of names in serialization
        use_enum_values=True,
        # Allow population by field name or alias
        populate_by_name=True,
        # Strict mode for better type checking
        str_strip_whitespace=True,
    )

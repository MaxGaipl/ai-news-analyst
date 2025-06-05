"""
Demonstration of enum serialization benefits in Pydantic.
"""

from enum import StrEnum
from pydantic import BaseModel, ConfigDict


# Example enum
class BiasRating(StrEnum):
    LEFT = "left"
    LEFT_CENTER = "left_center"
    CENTER = "center"
    RIGHT_CENTER = "right_center"
    RIGHT = "right"


# Model WITHOUT use_enum_values=True (default behavior)
class NewsSourceDefault(BaseModel):
    name: str
    bias: BiasRating


# Model WITH use_enum_values=True (our configuration)
class NewsSourceWithEnumValues(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    name: str
    bias: BiasRating


def demonstrate_enum_serialization():
    """Show the difference between enum serialization modes."""

    # Create instances
    source_default = NewsSourceDefault(name="BBC", bias=BiasRating.LEFT_CENTER)
    source_with_values = NewsSourceWithEnumValues(
        name="BBC", bias=BiasRating.LEFT_CENTER
    )

    print("🔍 ENUM SERIALIZATION DEMONSTRATION\n")

    print("1. DEFAULT BEHAVIOR (enum names):")
    print(f"   Python object: {source_default}")
    print(f"   JSON output:   {source_default.model_dump_json()}")
    print(f"   Dict output:   {source_default.model_dump()}")
    print()

    print("2. WITH use_enum_values=True (enum values):")
    print(f"   Python object: {source_with_values}")
    print(f"   JSON output:   {source_with_values.model_dump_json()}")
    print(f"   Dict output:   {source_with_values.model_dump()}")
    print()

    print("📊 PRACTICAL BENEFITS:")
    print()

    print("✅ API Responses:")
    print('   Default:     {"name": "BBC", "bias": "LEFT_CENTER"}  ← Python-style')
    print('   With values: {"name": "BBC", "bias": "left_center"}  ← Clean, consistent')
    print()

    print("✅ Database Storage:")
    print("   Values are stored as clean strings, not Python enum names")
    print("   Database queries work with actual values: WHERE bias = 'left_center'")
    print()

    print("✅ Frontend Integration:")
    print("   Frontend receives predictable, lowercase values")
    print("   No need to transform UPPER_CASE enum names")
    print()

    print("✅ External API Compatibility:")
    print("   Other systems expect clean values like 'center', not 'CENTER'")
    print("   Better integration with third-party services")


if __name__ == "__main__":
    demonstrate_enum_serialization()

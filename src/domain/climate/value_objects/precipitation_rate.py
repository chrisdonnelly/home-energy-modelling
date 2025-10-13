from dataclasses import dataclass


@dataclass(frozen=True)
class PrecipitationRate:
    """Precipitation rate value object in mm/h.

    Represents precipitation rate with validation.
    Precipitation rate is immutable and must be non-negative.

    Attributes:
        mm_per_h: The precipitation rate in mm/h (must be non-negative)
    """

    mm_per_h: float

    def __post_init__(self) -> None:
        if not isinstance(self.mm_per_h, (int, float)):
            raise ValueError("Precipitation rate must be a number")
        if self.mm_per_h < 0:
            raise ValueError("Precipitation rate must be non-negative")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.mm_per_h:.2f} mm/h"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"PrecipitationRate({self.mm_per_h})"

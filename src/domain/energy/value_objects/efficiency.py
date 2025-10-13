from dataclasses import dataclass


@dataclass(frozen=True)
class Efficiency:
    """Efficiency value object as a dimensionless ratio.

    Represents efficiency with validation.
    Efficiency is immutable and must be between 0 and 1.

    Attributes:
        ratio: The efficiency as a dimensionless ratio (must be between 0 and 1)
    """

    ratio: float

    def __post_init__(self) -> None:
        if not isinstance(self.ratio, (int, float)):
            raise ValueError("Efficiency must be a number")
        if self.ratio < 0 or self.ratio > 1:
            raise ValueError("Efficiency must be between 0 and 1")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.ratio:.2f} ratio"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Efficiency({self.ratio})"

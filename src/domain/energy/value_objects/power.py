from dataclasses import dataclass


@dataclass(frozen=True)
class Power:
    """Power value object in watts.

    Represents power with validation.
    Power is immutable and must be non-negative.

    Attributes:
        watts: The power in watts (must be non-negative)
    """

    watts: float

    def __post_init__(self) -> None:
        if not isinstance(self.watts, (int, float)):
            raise ValueError("Power must be a number")
        if self.watts < 0:
            raise ValueError("Power must be non-negative")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.watts:.2f} W"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Power({self.watts})"

from dataclasses import dataclass


@dataclass(frozen=True)
class Humidity:
    """Humidity value object in percent relative humidity.

    Represents relative humidity with validation.
    Humidity is immutable and must be between 0 and 100.

    Attributes:
        percent: The humidity in percent (must be between 0 and 100)
    """

    percent: float

    def __post_init__(self) -> None:
        if not isinstance(self.percent, (int, float)):
            raise ValueError("Humidity must be a number")
        if self.percent < 0 or self.percent > 100:
            raise ValueError("Humidity must be between 0 and 100")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.percent:.2f} %"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Humidity({self.percent})"

from dataclasses import dataclass


@dataclass(frozen=True)
class Pitch:
    """Pitch value object in degrees.

    Represents a physical pitch with validation.
    Pitches are immutable and must be between 0 and 360.
    """

    degrees: float

    def __post_init__(self) -> None:
        if not isinstance(self.degrees, (int, float)):
            raise ValueError("Pitch must be a number")
        if self.degrees < 0 or self.degrees > 360:
            raise ValueError("Pitch must be between 0 and 360")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.degrees:.2f} °"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Pitch({self.degrees})"

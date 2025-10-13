from dataclasses import dataclass


@dataclass(frozen=True)
class Energy:
    """Energy value object in joules.

    Represents energy with validation.
    Energy is immutable and must be non-negative.

    Attributes:
        joules: The energy in joules (must be non-negative)
    """

    joules: float

    def __post_init__(self) -> None:
        if not isinstance(self.joules, (int, float)):
            raise ValueError("Energy must be a number")
        if self.joules < 0:
            raise ValueError("Energy must be non-negative")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.joules:.2f} J"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Energy({self.joules})"

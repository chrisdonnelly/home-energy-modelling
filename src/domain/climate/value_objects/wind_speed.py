from dataclasses import dataclass


@dataclass(frozen=True)
class WindSpeed:
    """Wind speed value object in m/s.

    Represents wind speed with validation.
    Wind speed is immutable and must be non-negative.
    Attributes:
        m_per_s: The wind speed in m/s (must be positive)
    """

    m_per_s: float

    def __post_init__(self) -> None:
        if not isinstance(self.m_per_s, (int, float)):
            raise ValueError("Wind speed must be a number")
        if self.m_per_s < 0:
            raise ValueError("Wind speed must be non-negative")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.m_per_s:.2f} m/s"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"WindSpeed({self.m_per_s})"

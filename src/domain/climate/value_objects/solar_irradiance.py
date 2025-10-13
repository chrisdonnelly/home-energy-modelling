from dataclasses import dataclass


@dataclass(frozen=True)
class SolarIrradiance:
    """Solar irradiance value object in W/m².

    Represents solar irradiance with validation.
    Solar irradiance is immutable and must be positive.

    Attributes:
        w_per_m2: The solar irradiance in W/m² (must be positive)
    """

    w_per_m2: float

    def __post_init__(self) -> None:
        if not isinstance(self.w_per_m2, (int, float)):
            raise ValueError("Solar irradiance must be a number")
        if self.w_per_m2 <= 0:
            raise ValueError("Solar irradiance must be positive")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.w_per_m2:.2f} W/m²"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"SolarIrradiance({self.w_per_m2})"

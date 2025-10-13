import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ArealHeatCapacity:
    """Areal heat capacity value object in J/m²·K.

    Represents thermal mass per unit area with validation.
    Used specifically in Building domain for thermal mass calculations.
    Areal heat capacity is immutable and must be positive.

    Attributes:
        j_per_m2_k: The areal heat capacity in J/m²·K (must be positive)
    """

    j_per_m2_k: float

    def __post_init__(self) -> None:
        """Validate areal heat capacity after initialization."""
        if not isinstance(self.j_per_m2_k, (int, float)):
            raise ValueError("Areal heat capacity must be a number")

        if self.j_per_m2_k <= 0:
            raise ValueError("Areal heat capacity must be positive")

        if not math.isfinite(self.j_per_m2_k):
            raise ValueError("Areal heat capacity must be finite")

    @property
    def kj_per_m2_k(self) -> float:
        """Convert to kJ/m²·K."""
        return self.j_per_m2_k / 1000

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.j_per_m2_k:.0f} J/m²·K"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"ArealHeatCapacity({self.j_per_m2_k})"

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Density:
    """Density value object in kg/m³.

    Represents material density with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Density is immutable and must be positive.

    Attributes:
        kg_per_m3: The density in kg/m³ (must be positive)
    """

    kg_per_m3: float

    def __post_init__(self) -> None:
        """Validate density after initialization."""
        if not isinstance(self.kg_per_m3, (int, float)):
            raise ValueError("Density must be a number")

        if self.kg_per_m3 <= 0:
            raise ValueError("Density must be positive")

        if not math.isfinite(self.kg_per_m3):
            raise ValueError("Density must be finite")

    @property
    def kg_per_liter(self) -> float:
        """Convert to kg/L."""
        return self.kg_per_m3 / 1000

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.kg_per_m3:.1f} kg/m³"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Density({self.kg_per_m3})"

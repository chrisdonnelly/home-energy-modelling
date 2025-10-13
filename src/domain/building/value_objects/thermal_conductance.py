import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ThermalConductance:
    """Thermal conductance value object in W/K.

    Represents thermal conductance with validation.
    Thermal conductance is immutable and must be positive.

    Attributes:
        w_per_k: The thermal conductance in W/K (must be positive)
    """

    w_per_k: float

    def __post_init__(self) -> None:
        """Validate thermal conductance after initialization."""
        if not isinstance(self.w_per_k, (int, float)):
            raise ValueError("Thermal conductance must be a number")
        if self.w_per_k <= 0:
            raise ValueError("Thermal conductance must be positive")
        if not math.isfinite(self.w_per_k):
            raise ValueError("Thermal conductance must be finite")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.w_per_k:.2f} W/K"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"ThermalConductance({self.w_per_k})"

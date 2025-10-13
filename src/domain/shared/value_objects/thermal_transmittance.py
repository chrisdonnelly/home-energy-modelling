import math
from dataclasses import dataclass


@dataclass(frozen=True)
class ThermalTransmittance:
    """Thermal transmittance value object in W/m²·K.

    Represents U-value (thermal transmittance) with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Thermal transmittance is immutable and must be positive.

    Attributes:
        w_per_m2_k: The thermal transmittance in W/m²·K (must be positive)
    """

    w_per_m2_k: float

    def __post_init__(self) -> None:
        """Validate thermal transmittance after initialization."""
        if not isinstance(self.w_per_m2_k, (int, float)):
            raise ValueError("Thermal transmittance must be a number")

        if self.w_per_m2_k <= 0:
            raise ValueError("Thermal transmittance must be positive")

        if not math.isfinite(self.w_per_m2_k):
            raise ValueError("Thermal transmittance must be finite")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.w_per_m2_k:.2f} W/m²·K"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"ThermalTransmittance({self.w_per_m2_k})"

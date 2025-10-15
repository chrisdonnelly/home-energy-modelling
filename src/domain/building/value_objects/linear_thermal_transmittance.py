import math
from dataclasses import dataclass


@dataclass(frozen=True)
class LinearThermalTransmittance:
    """Linear thermal transmittance value object in W/m·K.

    Represents linear thermal transmittance with validation.
    Linear thermal transmittance is immutable and must be positive.

    Attributes:
        w_per_m_k: The linear thermal transmittance in W/m·K (must be positive)
    """

    w_per_m_k: float

    def __post_init__(self) -> None:
        """Validate linear thermal transmittance after initialization."""
        if not isinstance(self.w_per_m_k, (int, float)):
            raise ValueError("Linear thermal transmittance must be a number")
        if self.w_per_m_k < 0:
            raise ValueError("Linear thermal transmittance must be non-negative")
        if not math.isfinite(self.w_per_m_k):
            raise ValueError("Linear thermal transmittance must be finite")

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.w_per_m_k:.2f} W/m·K"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"LinearThermalTransmittance({self.w_per_m_k})"

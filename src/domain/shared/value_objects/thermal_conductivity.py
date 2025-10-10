from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ThermalConductivity:
    """Thermal conductivity value object in W/m·K.
    
    Represents thermal conductivity with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Thermal conductivity is immutable and must be positive.

    Attributes:
        w_per_m_k: The thermal conductivity in W/m·K (must be positive)
    """
    
    w_per_m_k: float
    
    def __post_init__(self) -> None:
        """Validate thermal conductivity after initialization."""
        if not isinstance(self.w_per_m_k, (int, float)):
            raise ValueError("Thermal conductivity must be a number")
        
        if self.w_per_m_k <= 0:
            raise ValueError("Thermal conductivity must be positive")
        
        if not math.isfinite(self.w_per_m_k):
            raise ValueError("Thermal conductivity must be finite")
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.w_per_m_k:.2f} W/m·K"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"ThermalConductivity({self.w_per_m_k})"

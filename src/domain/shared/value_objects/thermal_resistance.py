from dataclasses import dataclass
import math

@dataclass(frozen=True)
class ThermalResistance:
    """Thermal resistance value object in m²·K/W.
    
    Represents thermal resistance with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Thermal resistance is immutable and must be positive.

    Attributes:
        m2_k_per_w: The thermal resistance in m²·K/W (must be positive)
    """
    
    m2_k_per_w: float
    
    def __post_init__(self) -> None:
        """Validate thermal resistance after initialization."""
        if not isinstance(self.m2_k_per_w, (int, float)):
            raise ValueError("Thermal resistance must be a number")
        
        if self.m2_k_per_w <= 0:
            raise ValueError("Thermal resistance must be positive")
        
        if not math.isfinite(self.m2_k_per_w):
            raise ValueError("Thermal resistance must be finite")
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.m2_k_per_w:.2f} m²·K/W"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"ThermalResistance({self.m2_k_per_w})"
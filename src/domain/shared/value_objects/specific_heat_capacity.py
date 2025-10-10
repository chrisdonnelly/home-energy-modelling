from dataclasses import dataclass
import math


@dataclass(frozen=True)
class SpecificHeatCapacity:
    """Specific heat capacity value object in J/kg·K.
    
    Represents specific heat capacity with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Specific heat capacity is immutable and must be positive.

    Attributes:
        j_per_kg_k: The specific heat capacity in J/kg·K (must be positive)
    """
    
    j_per_kg_k: float
    
    def __post_init__(self) -> None:
        """Validate specific heat capacity after initialization."""
        if not isinstance(self.j_per_kg_k, (int, float)):
            raise ValueError("Specific heat capacity must be a number")
        
        if self.j_per_kg_k <= 0:
            raise ValueError("Specific heat capacity must be positive")
        
        if not math.isfinite(self.j_per_kg_k):
            raise ValueError("Specific heat capacity must be finite")
    
    @property
    def kj_per_kg_k(self) -> float:
        """Convert to kJ/kg·K."""
        return self.j_per_kg_k / 1000
    
    @property
    def kwh_per_kg_k(self) -> float:
        """Convert to kWh/kg·K."""
        return self.j_per_kg_k / 3600000
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.j_per_kg_k:.0f} J/kg·K"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"SpecificHeatCapacity({self.j_per_kg_k})"

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Pressure:
    """Pressure value object in Pascals.
    
    Represents pressure with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Pressure is immutable and must be non-negative.

    Attributes:
        pascals: The pressure in Pascals (must be non-negative)
    """
    
    pascals: float
    
    def __post_init__(self) -> None:
        """Validate pressure after initialization."""
        if not isinstance(self.pascals, (int, float)):
            raise ValueError("Pressure must be a number")
        
        if self.pascals < 0:
            raise ValueError("Pressure must be non-negative")
        
        if not math.isfinite(self.pascals):
            raise ValueError("Pressure must be finite")
    
    @property
    def kilopascals(self) -> float:
        """Convert to kPa."""
        return self.pascals / 1000
    
    @property
    def bar(self) -> float:
        """Convert to bar."""
        return self.pascals / 100000
    
    def __str__(self) -> str:
        """String representation for display."""
        if self.pascals >= 1000:
            return f"{self.kilopascals:.1f} kPa"
        else:
            return f"{self.pascals:.0f} Pa"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Pressure({self.pascals})"

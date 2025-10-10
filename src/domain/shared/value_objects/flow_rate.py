from dataclasses import dataclass
import math


@dataclass(frozen=True)
class FlowRate:
    """Flow rate value object in m³/s.
    
    Represents volumetric flow rate with validation.
    Used across Building, Energy, Climate, and Simulation domains.
    Flow rate is immutable and must be non-negative.

    Attributes:
        cubic_meters_per_second: The flow rate in m³/s (must be non-negative)
    """
    
    cubic_meters_per_second: float
    
    def __post_init__(self) -> None:
        """Validate flow rate after initialization."""
        if not isinstance(self.cubic_meters_per_second, (int, float)):
            raise ValueError("Flow rate must be a number")
        
        if self.cubic_meters_per_second < 0:
            raise ValueError("Flow rate must be non-negative")
        
        if not math.isfinite(self.cubic_meters_per_second):
            raise ValueError("Flow rate must be finite")
    
    @property
    def cubic_meters_per_hour(self) -> float:
        """Convert to m³/h."""
        return self.cubic_meters_per_second * 3600
    
    @property
    def liters_per_second(self) -> float:
        """Convert to L/s."""
        return self.cubic_meters_per_second * 1000
    
    @property
    def liters_per_hour(self) -> float:
        """Convert to L/h."""
        return self.cubic_meters_per_second * 3600000
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.cubic_meters_per_second:.2f} m³/s"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"FlowRate({self.cubic_meters_per_second})"

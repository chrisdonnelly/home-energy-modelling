from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Volume:
    """Volume value object in cubic meters.

    Represents a physical volume with validation and unit conversion.
    Volumes are immutable and cannot be negative or zero.

    Attributes:
        cubic_metres: The volume in cubic metres (must be positive).
    """
    cubic_metres: float
    
    def __post_init__(self) -> None:
        """Validate volume after initialization."""
        if not isinstance(self.cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        
        if self.cubic_meters <= 0:
            raise ValueError("Volume must be positive")
        
        if not math.isfinite(self.cubic_meters):
            raise ValueError("Volume must be finite")

    @property
    def cubic_feet(self) -> float:
        """Convert to cubic feet."""
        return self.cubic_meters * 35.315
    
    @property
    def liters(self) -> float:
        """Convert to liters."""
        return self.cubic_meters * 1000
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.cubic_meters:.2f} m³"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Volume({self.cubic_meters})"
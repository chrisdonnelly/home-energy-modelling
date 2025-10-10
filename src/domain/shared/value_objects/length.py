from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Length:
    """Length value object in meters.
    
    Represents a physical length with validation.
    Used across Building, Energy, and Climate domains.
    Lengths are immutable and cannot be negative or zero.

    Attributes:
        meters: The length in meters (must be positive)
    """
    
    meters: float
    
    def __post_init__(self) -> None:
        """Validate length after initialization."""
        if not isinstance(self.meters, (int, float)):
            raise ValueError("Length must be a number")
        
        if self.meters <= 0:
            raise ValueError("Length must be positive")
        
        if not math.isfinite(self.meters):
            raise ValueError("Length must be finite")
    
    @property
    def feet(self) -> float:
        """Convert to feet."""
        return self.meters * 3.281
    
    @property
    def centimeters(self) -> float:
        """Convert to centimeters."""
        return self.meters * 100
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.meters:.2f} m"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Length({self.meters})"
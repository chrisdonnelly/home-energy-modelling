from dataclasses import dataclass
import math


@dataclass(frozen=True)
class AirChangeRate:
    """Air change rate value object in 1/h (air changes per hour).
    
    Represents ventilation rate with validation.
    Used specifically in Building domain for ventilation calculations.
    Air change rate is immutable and must be non-negative.

    Attributes:
        changes_per_hour: The air change rate in 1/h (must be non-negative)
    """
    
    changes_per_hour: float
    
    def __post_init__(self) -> None:
        """Validate air change rate after initialization."""
        if not isinstance(self.changes_per_hour, (int, float)):
            raise ValueError("Air change rate must be a number")
        
        if self.changes_per_hour < 0:
            raise ValueError("Air change rate must be non-negative")
        
        if not math.isfinite(self.changes_per_hour):
            raise ValueError("Air change rate must be finite")
    
    @property
    def changes_per_second(self) -> float:
        """Convert to 1/s."""
        return self.changes_per_hour / 3600
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.changes_per_hour:.2f} ACH"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"AirChangeRate({self.changes_per_hour})"

from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Area:
    """Area value object in square meters.

    Represents a physical area with validation and unit conversion.
    Areas are immutable and cannot be negative or zero.

    Attributes:
        square_metres: The area in square metres (must be positive).
    """
    square_metres: float

    def __post_init__(self) -> None:
        if not isinstance(self.square_metres, (int, float)):
            raise ValueError("Area must be a number")
        if self.square_metres <= 0:
            raise ValueError("Area must be positive")
        if not math.isfinite(self.square_metres):
            raise ValueError("Area must be finite")
    
    @property
    def square_feet(self) -> float:
        """Convert area to square feet."""
        return self.square_metres * 10.7639
    
    @property
    def square_centimetres(self) -> float:
        """Convert area to square centimetres."""
        return self.square_metres
    
    def __str__(self) -> str:
        """Return a string representation of the area for display."""
        return f"{self.square_metres:.2f} m²"
    
    def __repr__(self) -> str:
        """Return a string representation of the area for debugging."""
        return f"Area(square_metres={self.square_metres})"

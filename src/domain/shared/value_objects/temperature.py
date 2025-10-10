from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Temperature:
    """Temperature value object in Celsius.

    Represents a physical temperature with validation.
    Used across Building, Energy, and Climate domains.
    Temperatures are immutable and must be finite.

    Attributes:
        celsius: The temperature in Celsius (must be finite)
    """
    celsius: float

    def __post_init__(self) -> None:
        """Validate temperature after initialization."""
        if not isinstance(self.celsius, (int, float)):
            raise ValueError("Temperature must be a number")
        if not math.isfinite(self.celsius):
            raise ValueError("Temperature must be finite")
    
    @property
    def fahrenheit(self) -> float:
        """Convert to Fahrenheit."""
        return self.celsius * 9/5 + 32
    
    @property
    def kelvin(self) -> float:
        """Convert to Kelvin."""
        return self.celsius + 273.15
    
    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.celsius:.2f} °C"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Temperature({self.celsius})"
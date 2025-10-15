from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class TimeStepDuration:
    """Time step duration value object as timedelta.

    Represents a time step with validation.
    Time step is immutable and must be a timedelta.

    Attributes:
        timedelta: The time step duration as timedelta
    """

    duration: timedelta

    def __post_init__(self) -> None:
        if not isinstance(self.duration, timedelta):
            raise ValueError("Time step must be a timedelta")
        if self.duration <= timedelta(seconds=0):
            raise ValueError("Time step must be positive")

    @property
    def hours(self) -> float:
        """Duration in hours."""
        return self.duration.total_seconds() / 3600

    def __str__(self) -> str:
        return str(self.duration)

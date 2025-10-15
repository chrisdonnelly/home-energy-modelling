from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SimulationTime:
    """Current simulation time value object as datetime.

    Represents a simulation time with validation.
    Simulation time is immutable and must be a datetime.

    Attributes:
        datetime: The simulation time as datetime
    """

    datetime: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.datetime, datetime):
            raise ValueError("Simulation time must be a datetime")

    @property
    def hour(self) -> int:
        """Hour of day (0-23)."""
        return self.datetime.hour

    def __str__(self) -> str:
        return self.datetime.isoformat()

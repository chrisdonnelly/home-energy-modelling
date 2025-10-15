from dataclasses import dataclass
from functools import cached_property
from uuid import UUID

from domain.simulation.value_objects import SimulationTime, TimeStepDuration


@dataclass
class SimulationClock:
    """Simulation clock entity.

    Represents a simulation clock with a start time, end time, and time step.

    Attributes:
        start_time: The start time of the simulation
        end_time: The end time of the simulation
        timestep_duration: The time step duration of the simulation
        current_time: The current time of the simulation
        current_timestep: The current time step of the simulation
    """

    id: UUID
    start_time: SimulationTime
    end_time: SimulationTime
    timestep_duration: TimeStepDuration
    current_time: SimulationTime
    current_timestep: int

    @cached_property
    def total_time_steps(self) -> int:
        """Total number of time steps in the simulation."""
        total_time_steps = (
            self.end_time.datetime - self.start_time.datetime
        ) / self.timestep_duration.duration
        return int(total_time_steps)

    def advance(self) -> None:
        """Advance the simulation clock to the next time step."""
        self.current_timestep += 1
        time_elapsed = self.current_timestep * self.timestep_duration.duration
        new_datetime = self.start_time.datetime + time_elapsed
        self.current_time = SimulationTime(datetime=new_datetime)

    def is_complete(self) -> bool:
        """Check if the simulation clock is complete."""
        return self.current_timestep > self.total_time_steps

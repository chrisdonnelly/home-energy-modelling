from datetime import datetime, timedelta
from functools import cached_property

class SimulationClock:
    def __init__(self, start_time: datetime, end_time: datetime, time_step_duration: timedelta):
        self.start_time = start_time
        self.end_time = end_time
        self.time_step_duration = time_step_duration
    
    @cached_property
    def total_time_steps(self):
        return (self.end_time - self.start_time) / self.time_step_duration

    
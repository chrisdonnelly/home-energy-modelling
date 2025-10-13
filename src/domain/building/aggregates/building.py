from dataclasses import dataclass
from functools import cached_property
from uuid import UUID

from domain.building.entities import BuildingElement, Zone
from domain.building.value_objects import Area, Volume
from domain.energy.value_objects import Power
from domain.shared.value_objects import ThermalResistance


@dataclass(frozen=True)
class Building:
    """Building aggregate root.

    Represents a complete building with multiple thermal zones.
    This is the aggregate root that ensures consistency accross
    all building-related entities and value objects.

    Attributes:
    """

    id: UUID
    name: str
    zones: list[Zone]

    @cached_property
    def total_floor_area(self) -> Area:
        """Total floor area of the building."""
        total_area = sum(zone.area.square_metres for zone in self.zones)
        return Area(square_metres=total_area)

    @cached_property
    def total_volume(self) -> Volume:
        """Total volume of the building."""
        total_volume = sum(zone.volume.cubic_metres for zone in self.zones)
        return Volume(cubic_metres=total_volume)

    @cached_property
    def building_elements(self) -> list[BuildingElement]:
        """Get all building elements across all zones."""
        return [element for zone in self.zones for element in zone.building_elements]

    def calculate_total_fabric_heat_loss(self) -> Power:
        """Calculate total fabric heat loss across all building elements.

        Returns:
            Total fabric heat loss in Watts as Power value object
        """
        total_fabric_heat_loss = sum(
            element.calculate_fabric_heat_loss().watts
            for element in self.building_elements
        )
        return Power(watts=total_fabric_heat_loss)

    def calculate_total_thermal_resistance(self) -> ThermalResistance:
        """Calculate total thermal resistance across all building elements."""
        # This would aggregate thermal resistance calculations
        # from all building elements in all zones
        # For now, return a placeholder value
        return ThermalResistance(m2_k_per_w=0.0)

    def validate_building_consistency(self) -> bool:
        """Validate that the building aggregate is internally consistent."""
        # Ensure zones don't overlap
        # Ensure building elements are properly assigned
        # Ensure thermal calculations are consistent
        # For now, return True as a placeholder
        return True

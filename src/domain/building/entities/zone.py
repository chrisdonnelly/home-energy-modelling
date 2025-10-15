from dataclasses import dataclass
from uuid import UUID

from domain.building.constants import (
    AIR_DENSITY_KG_PER_M3,
    AIR_SPECIFIC_HEAT_CAPACITY_J_PER_KG_K,
)
from domain.building.entities import BuildingElement
from domain.building.value_objects import (
    AirChangeRate,
    Area,
    ThermalConductance,
    Volume,
)
from domain.shared.value_objects import Temperature


@dataclass(frozen=True)
class Zone:
    """Thermal zone entity.

    Represents a thermal zone within a building with its associated
    building elements, ventilation, and thermal properties.

    Attributes:
        id: Unique identifier for the zone
        name: Human-readable name for the zone
        area: Useful floor area in square meters
        volume: Total volume in cubic meters
        building_elements: List of building elements associated with this zone
        ventilation_rate: Air change rate for ventilation
        temperature_setpoint: Target temperature for the zone
        thermal_bridges: List of pre-normalized thermal bridges as ThermalConductance value objects
    """

    id: UUID
    name: str
    area: Area
    volume: Volume
    building_elements: list[BuildingElement]
    ventilation_rate: AirChangeRate
    temperature_setpoint: Temperature
    thermal_bridges: list[ThermalConductance]

    def calculate_total_building_element_area(self) -> Area:
        """Calculate the total area of all building elements in the zone.

        Returns:
            The total area of all building elements in the zone in square meters as Area value object
        """
        total_area = sum(
            element.area.square_metres for element in self.building_elements
        )
        return Area(square_metres=total_area)

    def calculate_ventilation_heat_transfer_coefficient(self) -> ThermalConductance:
        """Calculate ventilation heat transfer coefficient.

        Based on volume and air change rate.

        Returns:
            Ventilation heat transfer coefficient in W/K as ThermalConductance value object
        """
        air_flow_rate = (
            self.ventilation_rate.changes_per_second * self.volume.cubic_metres / 3600
        )

        thermal_conductance = (
            air_flow_rate
            * AIR_DENSITY_KG_PER_M3
            * AIR_SPECIFIC_HEAT_CAPACITY_J_PER_KG_K
        )

        return ThermalConductance(w_per_k=thermal_conductance)

    def calculate_total_thermal_bridge_heat_transfer_coefficient(
        self,
    ) -> ThermalConductance:
        """Calculate total thermal bridge heat transfer coefficient.

        Returns:
            Total thermal bridge heat transfer coefficient in W/K as ThermalConductance value object
        """
        return ThermalConductance(
            w_per_k=sum(bridge.w_per_k for bridge in self.thermal_bridges)
        )

    def calculate_total_fabric_heat_transfer_coefficient(self) -> ThermalConductance:
        """Calculate total fabric heat transfer coefficient (W/K) across all building elements.

        This sums the heat transfer coefficients (area * U-value) for all building elements
        in the zone.

        Returns:
            Total fabric heat transfer coefficient in W/K as ThermalConductance value object
        """
        total_fabric_heat_transfer_coefficient = sum(
            element.calculate_fabric_heat_transfer_coefficient().w_per_k
            for element in self.building_elements
        )
        return ThermalConductance(w_per_k=total_fabric_heat_transfer_coefficient)

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.name} ({self.area.square_metres:.1f} m²)"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Zone(id={self.id}, name='{self.name}', area={self.area.square_metres:.1f}m²)"

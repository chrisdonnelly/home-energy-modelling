from dataclasses import dataclass
from functools import cached_property
from uuid import UUID

from domain.building.entities import BuildingElement, Zone
from domain.building.value_objects import Area, ThermalConductance, Volume
from domain.shared.value_objects import ThermalTransmittance


@dataclass(frozen=True)
class Building:
    """Building aggregate root.

    Represents a complete building with multiple thermal zones.
    This is the aggregate root that ensures consistency across
    all building-related entities and value objects.

    Attributes:
        id: Unique identifier for the building
        name: Human-readable name for the building
        zones: List of thermal zones within the building
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

    def calculate_total_fabric_heat_transfer_coefficient(self) -> ThermalConductance:
        """Calculate total fabric heat transfer coefficient (W/K) across all zones."""
        total_fabric_heat_transfer_coefficient = sum(
            zone.calculate_total_fabric_heat_transfer_coefficient().w_per_k
            for zone in self.zones
        )
        return ThermalConductance(w_per_k=total_fabric_heat_transfer_coefficient)

    def calculate_total_ventilation_heat_transfer_coefficient(
        self,
    ) -> ThermalConductance:
        """Calculate total ventilation heat transfer coefficient (W/K) across all zones."""
        total_ventilation_heat_transfer_coefficient = sum(
            zone.calculate_ventilation_heat_transfer_coefficient().w_per_k
            for zone in self.zones
        )
        return ThermalConductance(w_per_k=total_ventilation_heat_transfer_coefficient)

    def calculate_total_thermal_bridge_heat_transfer_coefficient(
        self,
    ) -> ThermalConductance:
        """Calculate total thermal bridge heat transfer coefficient (W/K) across all zones."""
        total_thermal_bridge_heat_transfer_coefficient = sum(
            zone.calculate_total_thermal_bridge_heat_transfer_coefficient().w_per_k
            for zone in self.zones
        )
        return ThermalConductance(
            w_per_k=total_thermal_bridge_heat_transfer_coefficient
        )

    def calculate_total_heat_transfer_coefficient(self) -> ThermalConductance:
        """Calculate total Heat Transfer Coefficient (HTC) in W/K.

        HTC = fabric HTC + ventilation HTC + thermal bridges

        Returns:
            Total Heat Transfer Coefficient (HTC) in W/K as ThermalConductance value object
        """
        fabric_htc = self.calculate_total_fabric_heat_transfer_coefficient().w_per_k
        ventilation_htc = (
            self.calculate_total_ventilation_heat_transfer_coefficient().w_per_k
        )
        thermal_bridges_htc = (
            self.calculate_total_thermal_bridge_heat_transfer_coefficient().w_per_k
        )
        return ThermalConductance(
            w_per_k=fabric_htc + ventilation_htc + thermal_bridges_htc
        )

    def calculate_heat_loss_parameter(self) -> ThermalTransmittance:
        """Calculate heat loss parameter (HLP) in W/m²·K.

        HLP = Total HTC / Total floor area

        Returns:
            Heat loss parameter in W/m²·K as ThermalTransmittance value object
        """
        total_htc = self.calculate_total_heat_transfer_coefficient().w_per_k
        area = self.total_floor_area.square_metres
        return ThermalTransmittance(w_per_m2_k=total_htc / area)

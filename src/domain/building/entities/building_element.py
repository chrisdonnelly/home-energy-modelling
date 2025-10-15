from dataclasses import dataclass
from uuid import UUID

from domain.building.enums import ThermalBoundaryType
from domain.building.services import ThermalCalculationService
from domain.building.value_objects import (
    Area,
    ArealHeatCapacity,
    Orientation,
    Pitch,
    ThermalConductance,
)
from domain.shared.value_objects import ThermalResistance, ThermalTransmittance


@dataclass(frozen=True)
class BuildingElement:
    """Building element entity.

    Represents a building element with validation.
    Building elements are immutable and must be valid.

    Attributes:
        id: Unique identifier for the building element
        name: Human-readable name for the element
        thermal_boundary_type: Thermal boundary condition type
        area: Area of the element in square meters
        thermal_resistance: Thermal resistance in m²·K/W
        thermal_mass: Areal heat capacity in J/m²·K
        orientation: Geographical azimuth angle in degrees
        pitch: Tilt angle from horizontal in degrees
    """

    id: UUID
    name: str
    thermal_boundary_type: ThermalBoundaryType
    area: Area
    thermal_resistance: ThermalResistance
    areal_heat_capacity: ArealHeatCapacity
    orientation: Orientation
    pitch: Pitch

    def calculate_u_value(self) -> ThermalTransmittance:
        """Calculate the U-value of the building element.

        Returns:
            U-value in W/m²·K as ThermalTransmittance value object
        """
        thermal_calculation_service = ThermalCalculationService()
        return thermal_calculation_service.calculate_u_value(
            construction_resistance=self.thermal_resistance,
            pitch=self.pitch,
            thermal_boundary_type=self.thermal_boundary_type,
        )

    def calculate_fabric_heat_transfer_coefficient(self) -> ThermalConductance:
        """Calculate fabric heat transfer coefficient (W/K) for the building element.

        This is area * U-value, which giver the heat transfer coefficient in W/K.

        Returns:
            Fabric heat transfer coefficient in W/K as ThermalConductance value object
        """
        u_value = self.calculate_u_value()
        fabric_heat_transfer_coefficient = self.area.square_metres * u_value.w_per_m2_k
        return ThermalConductance(w_per_k=fabric_heat_transfer_coefficient)

    def __str__(self) -> str:
        """String representation for display."""
        return f"{self.name} ({self.thermal_boundary_type.value})"

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"BuildingElement(id={self.id}, name='{self.name}', type={self.thermal_boundary_type.value})"

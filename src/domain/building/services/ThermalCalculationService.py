from domain.building.constants import (
    PITCH_LIMIT_HORIZ_CEILING,
    PITCH_LIMIT_HORIZ_FLOOR,
    R_CURTAINS_BLINDS,
    R_SE,
    R_SI_DOWNWARDS,
    R_SI_HORIZONTAL,
    R_SI_UPWARDS,
)
from domain.building.enums import ThermalBoundaryType
from domain.building.value_objects import Pitch
from domain.shared.value_objects import ThermalResistance, ThermalTransmittance


class ThermalCalculationService:
    """Domain service for thermal calculations.

    Encapsulates building physics calculations that don't belong to a single entity.
    """

    def calculate_internal_surface_resistance(self, pitch: Pitch) -> ThermalResistance:
        """Calculate internal surface resistance based on pitch.

        Args:
            pitch: The pitch of the building element

        Returns:
            The internal surface resistance in m²·K/W as ThermalResistance value object
        """
        if PITCH_LIMIT_HORIZ_CEILING <= pitch.degrees <= PITCH_LIMIT_HORIZ_FLOOR:
            resistance_value = R_SI_HORIZONTAL
        elif pitch.degrees < PITCH_LIMIT_HORIZ_CEILING:
            resistance_value = R_SI_UPWARDS
        else:
            resistance_value = R_SI_DOWNWARDS

        return ThermalResistance(m2_k_per_w=resistance_value)

    def calculate_u_value(
        self,
        construction_resistance: ThermalResistance,
        pitch: Pitch,
        thermal_boundary_type: ThermalBoundaryType,
    ) -> ThermalTransmittance:
        """Calculate the u-value of a building element, including the internal surface resistance.

        Args:
            construction_resistance: The thermal resistance of the construction
            pitch: The pitch of the building element
            thermal_boundary_type: The thermal boundary type of the building element

        Returns:
            The u-value of the building element in W/m²·K as ThermalTransmittance value object
        """
        if thermal_boundary_type == ThermalBoundaryType.GROUND_CONTACT:
            return ThermalTransmittance(w_per_m2_k=construction_resistance.m2_k_per_w)

        if thermal_boundary_type == ThermalBoundaryType.INTERNAL_PARTITION:
            return ThermalTransmittance(w_per_m2_k=0.0)

        r_si = self.calculate_internal_surface_resistance(pitch=pitch)

        total_resistance = construction_resistance.m2_k_per_w + r_si.m2_k_per_w + R_SE

        if thermal_boundary_type == ThermalBoundaryType.EXTERNAL_GLAZING:
            total_resistance += R_CURTAINS_BLINDS

        u_value = 1.0 / total_resistance

        return ThermalTransmittance(w_per_m2_k=u_value)

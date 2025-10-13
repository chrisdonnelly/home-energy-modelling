from enum import Enum


class ThermalBoundaryType(Enum):
    """Thermal boundary type enumeration.

    These represent the 5 fundamental thermal boundary conditions in building physics.
    Each determines the heat transfer characteristics, external environment, and solar interaction.
    """

    EXTERNAL_SOLID = "external_solid"  # Outside environment, absorbs solar radiation
    EXTERNAL_GLAZING = (
        "external_glazing"  # Outside environment, transmits solar radiation
    )
    GROUND_CONTACT = "ground_contact"  # Ground environment, no solar interaction
    INTERNAL_PARTITION = "internal_partition"  # Conditioned space, no solar interaction
    UNHEATED_SPACE = "unheated_space"  # Unconditioned space, no solar interaction

    def __str__(self) -> str:
        """String representation for display."""
        return self.value.replace("_", " ").title()

"""Building physics constants from BS EN ISO 13789:2017, Table 8.

These are immutable constants used in thermal calculations.

References:
- BS EN ISO 13789:2017, Table 8: Conventional surface heat transfer coefficients
- BR 443: The values under "horizontal" apply to heat flow directions +/- 30 degrees from horizontal plane
"""

# Heat transfer coefficients (W/m²·K)
# Values from BS EN ISO 13789:2017, Table 8: Conventional surface heat transfer coefficients
H_CI_UPWARDS = 5.0  # Internal convective heat transfer coefficient, upwards heat flow
H_CI_HORIZONTAL = (
    2.5  # Internal convective heat transfer coefficient, horizontal heat flow
)
H_CI_DOWNWARDS = (
    0.7  # Internal convective heat transfer coefficient, downwards heat flow
)
H_CE = 20.0  # External convective heat transfer coefficient
H_RI = 5.13  # Internal radiative heat transfer coefficient
H_RE = 4.14  # External radiative heat transfer coefficient

# Pitch limits for heat flow direction classification (degrees)
# From BR 443: The values under "horizontal" apply to heat flow directions +/- 30 degrees from horizontal plane
PITCH_LIMIT_HORIZ_CEILING = 60.0  # Upper limit for horizontal classification
PITCH_LIMIT_HORIZ_FLOOR = 120.0  # Lower limit for horizontal classification

# Surface resistances of building elements, in m²·K/W
# Calculated from heat transfer coefficients: R = 1 / (H_conv + H_rad)
R_SI_HORIZONTAL = 1.0 / (
    H_RI + H_CI_HORIZONTAL
)  # Internal surface resistance, horizontal
R_SI_UPWARDS = 1.0 / (H_RI + H_CI_UPWARDS)  # Internal surface resistance, upwards
R_SI_DOWNWARDS = 1.0 / (H_RI + H_CI_DOWNWARDS)  # Internal surface resistance, downwards
R_SE = 1.0 / (H_CE + H_RE)  # External surface resistance

# Window treatment resistance
# From SAP 10.2 specification, paragraph 3.2
# Effective window U-value includes assumed use of curtains/blinds
R_CURTAINS_BLINDS = 0.04  # m²K/W - Thermal resistance of curtains/blinds

# Air properties for ventilation calculations
# These appear to be standard atmospheric air properties at ~20°C, 1 atm
AIR_DENSITY_KG_PER_M3 = 1.204  # kg/m³ (0.001204 kg/litre × 1000)
AIR_SPECIFIC_HEAT_CAPACITY_J_PER_KG_K = 1006.0  # J/kg·K

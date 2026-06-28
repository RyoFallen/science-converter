"""Core conversion logic for the Science Converter.

Provides conversions for physical quantities: length, mass and temperature.
Each public function raises ValueError on unknown units so the CLI and the
test-suite can rely on predictable error handling.
"""

# Conversion factors expressed relative to a base unit.
# Length base unit: metre.
_LENGTH_TO_METRE = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}

# Mass base unit: gram.
_MASS_TO_GRAM = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "t": 1_000_000.0,
    "oz": 28.349523125,
    "lb": 453.59237,
}


def _convert_linear(value, from_unit, to_unit, table, kind):
    """Convert a value using a base-unit factor table."""
    try:
        from_factor = table[from_unit]
        to_factor = table[to_unit]
    except KeyError as exc:
        raise ValueError(f"Unknown {kind} unit: {exc.args[0]!r}") from None
    return value * from_factor / to_factor


def convert_length(value, from_unit, to_unit):
    """Convert a length between supported units (mm, cm, m, km, in, ft, mi)."""
    return _convert_linear(value, from_unit, to_unit, _LENGTH_TO_METRE, "length")


def convert_mass(value, from_unit, to_unit):
    """Convert a mass between supported units (mg, g, kg, t, oz, lb)."""
    return _convert_linear(value, from_unit, to_unit, _MASS_TO_GRAM, "mass")


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between Celsius, Fahrenheit and Kelvin.

    Units are given as single letters: 'C', 'F' or 'K' (case-insensitive).
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    valid = {"C", "F", "K"}
    if from_unit not in valid or to_unit not in valid:
        raise ValueError("Temperature units must be one of: C, F, K")

    # Normalise to Celsius first.
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:  # Kelvin
        celsius = value - 273.15

    # Convert Celsius to the target unit.
    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15  # Kelvin


def supported_units():
    """Return a mapping of category -> supported unit symbols."""
    return {
        "length": sorted(_LENGTH_TO_METRE),
        "mass": sorted(_MASS_TO_GRAM),
        "temperature": ["C", "F", "K"],
    }

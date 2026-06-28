"""Fuel-consumption conversions for the Science Converter.

Adds support for converting between the two most common ways of expressing
fuel economy:

- ``L/100km``  -> litres consumed per 100 kilometres (lower is better)
- ``mpg``      -> miles per US gallon (higher is better)

The two scales are inversely related, so this module also exposes a single
``convert_fuel`` entry point that mirrors the style of the core converter.
"""

# 1 US gallon = 3.785411784 litres, 1 mile = 1.609344 km.
_LITRES_PER_GALLON = 3.785411784
_KM_PER_MILE = 1.609344

# mpg * THIS_CONSTANT == L/100km (and vice-versa, since the relation is symmetric).
_MPG_L100_CONSTANT = (_LITRES_PER_GALLON * 100) / (_KM_PER_MILE)


def mpg_to_l100km(mpg):
    """Convert miles-per-gallon to litres-per-100km."""
    if mpg <= 0:
        raise ValueError("mpg must be a positive number")
    return _MPG_L100_CONSTANT / mpg


def l100km_to_mpg(l100km):
    """Convert litres-per-100km to miles-per-gallon."""
    if l100km <= 0:
        raise ValueError("L/100km must be a positive number")
    return _MPG_L100_CONSTANT / l100km


def convert_fuel(value, from_unit, to_unit):
    """Convert a fuel-economy value between 'mpg' and 'l100km'.

    Unit names are case-insensitive. Passing the same unit returns the value
    unchanged.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    valid = {"mpg", "l100km"}
    if from_unit not in valid or to_unit not in valid:
        raise ValueError("Fuel units must be one of: mpg, l100km")

    if from_unit == to_unit:
        return value
    if from_unit == "mpg":
        return mpg_to_l100km(value)
    return l100km_to_mpg(value)

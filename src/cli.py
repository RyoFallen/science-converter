"""Command-line interface for the Science Converter.

Usage examples:
    python -m src.cli length 10 km mi
    python -m src.cli temperature 100 C F
    python -m src.cli mass 5 kg lb
    python -m src.cli fuel 30 mpg l100km
"""

import argparse
import sys

from . import converter, fuel


def build_parser():
    parser = argparse.ArgumentParser(
        prog="science-converter",
        description="Science Converter — convert physical units (length, mass, temperature, fuel) from the command line.",
    )
    parser.add_argument(
        "category",
        choices=["length", "mass", "temperature", "fuel"],
        help="Quantity to convert.",
    )
    parser.add_argument("value", type=float, help="Numeric value to convert.")
    parser.add_argument("from_unit", help="Source unit.")
    parser.add_argument("to_unit", help="Target unit.")
    return parser


_DISPATCH = {
    "length": converter.convert_length,
    "mass": converter.convert_mass,
    "temperature": converter.convert_temperature,
    "fuel": fuel.convert_fuel,
}


def main(argv=None):
    args = build_parser().parse_args(argv)
    func = _DISPATCH[args.category]
    try:
        result = func(args.value, args.from_unit, args.to_unit)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"{args.value} {args.from_unit} = {result:g} {args.to_unit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

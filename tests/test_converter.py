"""Unit tests for the core converter module."""

import math
import unittest

from src import converter


class TestLength(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertAlmostEqual(converter.convert_length(1, "km", "mi"), 0.621371, places=5)

    def test_metre_to_cm(self):
        self.assertAlmostEqual(converter.convert_length(2, "m", "cm"), 200.0)

    def test_inch_to_cm(self):
        self.assertAlmostEqual(converter.convert_length(1, "in", "cm"), 2.54)

    def test_identity(self):
        self.assertEqual(converter.convert_length(5, "m", "m"), 5)

    def test_unknown_unit_raises(self):
        with self.assertRaises(ValueError):
            converter.convert_length(1, "m", "lightyear")


class TestMass(unittest.TestCase):
    def test_kg_to_lb(self):
        self.assertAlmostEqual(converter.convert_mass(1, "kg", "lb"), 2.204623, places=5)

    def test_g_to_kg(self):
        self.assertAlmostEqual(converter.convert_mass(2500, "g", "kg"), 2.5)

    def test_unknown_unit_raises(self):
        with self.assertRaises(ValueError):
            converter.convert_mass(1, "stone", "kg")


class TestTemperature(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(converter.convert_temperature(100, "C", "F"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(converter.convert_temperature(32, "F", "C"), 0.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(converter.convert_temperature(0, "C", "K"), 273.15)

    def test_case_insensitive(self):
        self.assertAlmostEqual(converter.convert_temperature(0, "c", "k"), 273.15)

    def test_unknown_unit_raises(self):
        with self.assertRaises(ValueError):
            converter.convert_temperature(0, "C", "X")


class TestMetadata(unittest.TestCase):
    def test_supported_units(self):
        units = converter.supported_units()
        self.assertIn("length", units)
        self.assertIn("mass", units)
        self.assertIn("temperature", units)
        self.assertTrue(math.isclose(len(units["temperature"]), 3))


if __name__ == "__main__":
    unittest.main()

"""Unit tests for the fuel-consumption module."""

import unittest

from src import fuel


class TestFuelConversion(unittest.TestCase):
    def test_mpg_to_l100km_known_value(self):
        # ~30 mpg is roughly 7.84 L/100km.
        self.assertAlmostEqual(fuel.mpg_to_l100km(30), 7.8402, places=3)

    def test_l100km_to_mpg_known_value(self):
        self.assertAlmostEqual(fuel.l100km_to_mpg(7.8402), 30.0, places=2)

    def test_round_trip(self):
        original = 45.0
        converted = fuel.mpg_to_l100km(original)
        self.assertAlmostEqual(fuel.l100km_to_mpg(converted), original, places=6)

    def test_convert_fuel_dispatch(self):
        self.assertAlmostEqual(
            fuel.convert_fuel(30, "mpg", "l100km"), 7.8402, places=3
        )

    def test_convert_fuel_identity(self):
        self.assertEqual(fuel.convert_fuel(25, "mpg", "mpg"), 25)

    def test_convert_fuel_case_insensitive(self):
        self.assertAlmostEqual(
            fuel.convert_fuel(30, "MPG", "L100KM"), 7.8402, places=3
        )

    def test_non_positive_raises(self):
        with self.assertRaises(ValueError):
            fuel.mpg_to_l100km(0)
        with self.assertRaises(ValueError):
            fuel.l100km_to_mpg(-5)

    def test_unknown_unit_raises(self):
        with self.assertRaises(ValueError):
            fuel.convert_fuel(10, "mpg", "kmpl")


if __name__ == "__main__":
    unittest.main()

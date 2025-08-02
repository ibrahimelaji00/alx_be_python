# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Initialise une instance avant chaque test."""
        self.calc = SimpleCalculator()

    # ---- Tests pour add ----
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, 2), -3)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=7)
        self.assertAlmostEqual(self.calc.add(-1.2, -3.8), -5.0, places=7)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # ---- Tests pour subtract ----
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtract_negative_and_positive(self):
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(2, -3), 5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)
        self.assertAlmostEqual(self.calc.subtract(-1.5, -2.5), 1.0, places=7)

    # ---- Tests pour multiply ----
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2), -3.0, places=7)

    # ---- Tests pour divide ----
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0), "Diviser par zéro doit retourner None")

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75, places=7)
        self.assertAlmostEqual(self.calc.divide(5, 2.5), 2.0, places=7)

    # ---- Tests combinés / limites ----
    def test_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)

    def test_zero_behavior(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertIsNone(self.calc.divide(0, 0))  # conventionnellement None pour 0/0 dans cette classe

if __name__ == "__main__":
    unittest.main()

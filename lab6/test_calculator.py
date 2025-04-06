import unittest
from my_calculator import Calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(7, 8), 15)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(7, 3), 4)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(7, 7), 49)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(30, 6), 5)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)

    def test_power(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)

    def test_sqrt(self):
        calc = Calculator()
        self.assertEqual(calc.sqrt(25), 5)
        with self.assertRaises(ValueError):
            calc.sqrt(-1)

    def test_log(self):
        calc = Calculator()
        self.assertAlmostEqual(calc.log(100, 10), 2)
        with self.assertRaises(ValueError):
            calc.log(-1, 10)


# Created by Leon Hunter at 9:54 AM 10/23/2020
import unittest
from src.main.calculator import Calculator

NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE = 'incorrect value'


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # given
        expected_calculation = 5.0

        # when
        actual_calculation = self.calc.add(NUMBER_1, NUMBER_2)

        # then
        self.assertEqual(expected_calculation, actual_calculation, FAILURE)

    def test_subtract(self):
        # given
        expected_calculation = 1.0

        # when
        actual_calculation = self.calc.subtract(NUMBER_1, NUMBER_2)

        # then
        self.assertEqual(expected_calculation, actual_calculation, FAILURE)

    def test_subtract_negative(self):
        # given
        expected_calculation = -1.0

        # when
        actual_calculation = self.calc.subtract(NUMBER_2, NUMBER_1)

        # then
        self.assertEqual(expected_calculation, actual_calculation, FAILURE)

    def test_multiply(self):
        # given
        expected_calculation = 6.0

        # when
        actual_calculation = self.calc.multiply(NUMBER_1, NUMBER_2)

        # then
        self.assertEqual(expected_calculation, actual_calculation, FAILURE)

    def test_divide(self):
        # given
        expected_calculation = 1.5

        # when
        actual_calculation = self.calc.divide(NUMBER_1, NUMBER_2)

        # then
        self.assertEqual(expected_calculation, actual_calculation, FAILURE)

    def test_divide_by_zero(self):
        # given
        expected_calculation = ZeroDivisionError

        # when
        actual_calculation = self.calc.divide()

        # then
        self.assertRaises(expected_calculation, actual_calculation, NUMBER_1, 0)

# Created by Leon Hunter at 11:23 AM 10/24/2020
from unittest import TestCase

from calculator import Calculator

error_message = 'incorrect_value'


class CalculationTester(TestCase):
    def __init__(self, method_to_be_tested, value_sets):
        super(CalculationTester, self).__init__()
        self.value_sets = value_sets
        self.method_to_test = method_to_be_tested

    def test_value_sets(self):
        for value_set in self.value_sets:
            # given
            first_value = value_set[0]
            second_value = value_set[1]
            expected_calculation = value_set[2]

            # when
            actual_calculation = self.method_to_test(first_value, second_value)

            # then
            self.assertAlmostEqual(expected_calculation, actual_calculation, error_message)


class AddTester(CalculationTester):
    def __init__(self):
        super().__init__(Calculator().add, [
            (1, 3, 4),
            (5, 8, 13),
            (13, 21, 34),
            (0, 0, 0),
            (3, 1, 4),
            (8, 5, 13),
            (21, 13, 34),
        ])


class SubtractTester(CalculationTester):
    def __init__(self):
        super().__init__(Calculator().subtract, [
            (1, 3, -2),
            (5, 8, -3),
            (13, 21, -8),
            (0, 0, 0),
            (3, 1, 2),
            (8, 5, 3),
            (21, 13, 8),
        ])


class MultiplyTester(CalculationTester):
    def __init__(self):
        super().__init__(Calculator().multiply, [
            (1, 3, 3),
            (5, 8, 40),
            (13, 21, 273),
            (0, 0, 0),
            (3, 1, 3),
            (8, 5, 40),
            (21, 13, 273),
        ])


class DivideTester(CalculationTester):
    def __init__(self):
        super().__init__(Calculator().divide, [
            (1, 3, .333),
            (5, 8, .625),
            (13, 21, .619),
            (0, 0, ZeroDivisionError),
            (3, 1, 3),
            (8, 5, 1.6),
            (21, 13, 1.615),
        ])

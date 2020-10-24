# Created by Leon Hunter at 11:23 AM 10/24/2020
from unittest import TestCase

from predicator import Predicator

error_message = 'incorrect_value'


class PredicatorTester(TestCase):
    def __init__(self, method_to_be_tested, value_sets):
        self.value_sets = value_sets
        self.method_to_test = method_to_be_tested

    def test_value_sets(self):
        for value_set in self.value_sets:
            # given
            first_value = value_set[0]
            expected_calculation = value_set[1]

            # when
            actual_calculation = self.method_to_test(first_value)

            # then
            self.assertAlmostEqual(expected_calculation, actual_calculation, error_message)


class IsGreaterThan5Test(PredicatorTester):
    def __init__(self):
        super().__init__(Predicator().is_greater_than_5, [
            (1, False),
            (5, False),
            (6, True),
            (7, True)
        ])


class IsGreaterThan8Test(PredicatorTester):
    def __init__(self):
        super().__init__(Predicator().is_greater_than_8, [
            (1, False),
            (8, False),
            (10, True),
            (17, True)
        ])


class IsLessThan1(PredicatorTester):
    def __init__(self):
        super().__init__(Predicator().is_less_than_1, [
            (5, False),
            (1, False),
            (-6, True),
            (-7, True)
        ])


class IsLessThan4(PredicatorTester):
    def __init__(self):
        super().__init__(Predicator().is_less_than_4, [
            (5, False),
            (4, False),
            (2, True),
            (-7, True)
        ])

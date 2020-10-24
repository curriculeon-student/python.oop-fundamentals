# Created by Leon Hunter at 3:57 PM 10/23/2020
from unittest import TestCase

from string_manipulator import StringManipulator


class StringManipulatorTest(TestCase):
    def _test_nullary_function(self, method_to_be_tested, value_sets):
        for value_set in value_sets:
            # given
            expected_output = value_set[0]

            # when
            actual_output = method_to_be_tested()

            calculation_error_message = '''            
            expected_output = {}
            actual_output = {}
            '''.format(expected_output, actual_output)

            # then
            self.assertEquals(expected_output, actual_output, calculation_error_message)

    def _test_unary_function(self, method_to_be_tested, value_sets):
        for value_set in value_sets:
            # given
            first_value = value_set[0]
            expected_output = value_set[2]

            # when
            actual_output = method_to_be_tested(first_value)

            calculation_error_message = '''
            first_value = {}
            expected_output = {}
            actual_output = {}
            '''.format(first_value, expected_output, actual_output)

            # then
            self.assertEquals(expected_output, actual_output, calculation_error_message)

    def _test_binary_function(self, method_to_be_tested, value_sets):
        for value_set in value_sets:
            # given
            first_value = value_set[0]
            second_value = value_set[1]
            expected_output = value_set[2]

            # when
            actual_output = method_to_be_tested(first_value, second_value)

            calculation_error_message = '''
            first_value = {}
            second_value = {}            
            expected_output = {}
            actual_output = {}
            '''.format(first_value, second_value, expected_output, actual_output)

            # then
            self.assertEquals(expected_output, actual_output, calculation_error_message)

    def _test_ternary_function(self, method_to_be_tested, value_sets):
        for value_set in value_sets:
            # given
            first_value = value_set[0]
            second_value = value_set[1]
            third_value = value_set[2]
            expected_output = value_set[3]

            # when
            actual_output = method_to_be_tested(first_value, second_value, third_value)

            calculation_error_message = '''
            first_value = {}
            second_value = {}
            third_value = {}
            expected_output = {}
            actual_output = {}
            '''.format(first_value, second_value, third_value, expected_output, actual_output)

            # then
            self.assertEquals(expected_output, actual_output, calculation_error_message)

    def test_substring_inclusive(self):
        self._test_ternary_function(StringManipulator().substring_inclusive, [
            ("Hello", 0, 4, "Hello"),
            ("Hello", 0, 3, "Hell"),
            ("Hello", 1, 4, "ello"),
        ])

    def test_substring_exclusive(self):
        self._test_ternary_function(StringManipulator().substring_exclusive, [
            ("Hello", 0, 4, "ell"),
            ("Hello", 0, 3, "el"),
            ("Hello", 1, 4, "ll")
        ])

    def test_concatenate(self):
        self._test_binary_function(StringManipulator().concatenate, [
            ("Hello", "World", "HelloWorld"),
            (19, 93, "1993"),
            (19, "", "19"),
            (None, "None", "NoneNone")
        ])

    def test_compare(self):
        self._test_binary_function(StringManipulator().compare, [
            ("Hello", 0, False),
            ("Hello", "Hello", True),
            ("0", 0, True),
            (None, 0, True),
            (False, 0, True),
            (True, 1, True)
        ])



    def test_get_first_word(self):
        self._test_unary_function(StringManipulator().get_first_word, [
            ("The quick brown fox", "The"),
            ("Quick Brown Fox", "Quick"),
            ("Brown Fox", "Brown"),
        ])

    def test_get_second_word(self):
        self._test_unary_function(StringManipulator().get_second_word, [
            ("The quick brown fox", "quick"),
            ("Quick Brown Fox", "Brown"),
            ("Brown Fox", "Fox"),
        ])


    def test_get_hello_world(self):
        self._test_nullary_function(StringManipulator().get_hello_world, [["Hello World"]])

import unittest
from practice import ListCalculator

class TestListCalculator(unittest.TestCase):
    def test_lists_division_normal_case(self):
        # Normal case where both lists have non-zero sums
        x_values = [10, 20, 30]
        y_values = [10, 20, 30]

        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()

        self.assertEqual(result, 1)

    def test_lists_division_negative_numbers_case(self):
        # Normal case where both lists have non-zero sums
        x_values = [-10, -20, -30]
        y_values = [-10, -20, -30]

        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

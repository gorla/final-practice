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

    def test_list_y_zero(self):
        # Edge case where sum of x_values is zero
        y_values = [3, 5, 7]
        x_values = [5, -4, -1]
        
        calculator = ListCalculator(x_values, y_values)
        result = calculator.lists_division()
        
if __name__ == '__main__':
    unittest.main()

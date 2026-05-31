import unittest

from calculations import calculate_result, format_number


class TestCalculations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculate_result("Sum", [1.0, 2.0, 3.0]), 6.0)

    def test_average(self):
        self.assertEqual(calculate_result("Average", [2.0, 4.0, 6.0]), 4.0)

    def test_minimum(self):
        self.assertEqual(calculate_result("Minimum", [3.0, 1.0, 2.0]), 1.0)

    def test_maximum(self):
        self.assertEqual(calculate_result("Maximum", [3.0, 1.0, 2.0]), 3.0)

    def test_product(self):
        self.assertEqual(calculate_result("Product", [2.0, 3.0, 4.0]), 24.0)

    def test_unknown_operation_defaults_to_sum(self):
        self.assertEqual(calculate_result("Unknown", [1.0, 2.0]), 3.0)

    def test_format_whole_number(self):
        self.assertEqual(format_number(5.0), "5")

    def test_format_decimal_number(self):
        self.assertEqual(format_number(2.5), "2.5")


if __name__ == "__main__":
    unittest.main()

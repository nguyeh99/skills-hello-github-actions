import unittest
from average import calculate_average, calculate_maximum


class TestCalculateAverage(unittest.TestCase):
    """Unit tests for the calculate_average function"""

    def test_normal_average(self):
        """Test calculating average of regular numbers"""
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_empty_list(self):
        """Test that empty list returns 0"""
        self.assertEqual(calculate_average([]), 0)

    def test_single_number(self):
        """Test average of a single number"""
        self.assertEqual(calculate_average([5]), 5)

    def test_negative_numbers(self):
        """Test average with negative numbers"""
        self.assertEqual(calculate_average([-10, -20, -30]), -20)

    def test_mixed_positive_negative(self):
        """Test average with mixed positive and negative numbers"""
        self.assertEqual(calculate_average([-10, 10]), 0)

    def test_decimal_numbers(self):
        """Test average with decimal numbers"""
        result = calculate_average([1.5, 2.5, 3.0])
        self.assertAlmostEqual(result, 2.333333, places=5)

    def test_two_numbers(self):
        """Test average of two numbers"""
        self.assertEqual(calculate_average([5, 15]), 10)

    def test_large_numbers(self):
        """Test average with large numbers"""
        self.assertEqual(calculate_average([1000000, 2000000, 3000000]), 2000000)


class TestCalculateMaximum(unittest.TestCase):
    """Unit tests for the calculate_maximum function"""

    def test_normal_maximum(self):
        """Test finding maximum of regular numbers"""
        self.assertEqual(calculate_maximum([10, 20, 30]), 30)

    def test_empty_list(self):
        """Test that empty list returns None"""
        self.assertIsNone(calculate_maximum([]))

    def test_single_number(self):
        """Test maximum of a single number"""
        self.assertEqual(calculate_maximum([5]), 5)

    def test_negative_numbers(self):
        """Test maximum with all negative numbers"""
        self.assertEqual(calculate_maximum([-10, -20, -30]), -10)

    def test_mixed_positive_negative(self):
        """Test maximum with mixed positive and negative numbers"""
        self.assertEqual(calculate_maximum([-10, 5, 20]), 20)

    def test_decimal_numbers(self):
        """Test maximum with decimal numbers"""
        self.assertEqual(calculate_maximum([1.5, 2.5, 3.0]), 3.0)

    def test_two_numbers(self):
        """Test maximum of two numbers"""
        self.assertEqual(calculate_maximum([5, 15]), 15)

    def test_large_numbers(self):
        """Test maximum with large numbers"""
        self.assertEqual(calculate_maximum([1000000, 3000000, 2000000]), 3000000)

    def test_duplicates(self):
        """Test maximum when values are duplicated"""
        self.assertEqual(calculate_maximum([5, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()

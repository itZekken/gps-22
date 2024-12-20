import unittest
import transform


"""This module contains test cases for string transformation functions
from the transform module, such as to_upper_case, to_lower_case, and 
to_capitalize. These functions are tested to ensure they behave as expected."""

class TestStringMethods(unittest.TestCase):
    """Test cases for string transformation functions in the transform module."""

    def test_is_upper(self):
        """Test if the to_upper_case function correctly converts a string to uppercase."""
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """Test if the to_lower_case function correctly converts a string to lowercase."""
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """Test if the to_capitalize function correctly capitalizes a string."""
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()

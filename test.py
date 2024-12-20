"""Module providing a function printing python version."""
import unittest
import transform


"""Tests"""

class TestStringMethods(unittest.TestCase):
    """Test transformacio de strings."""

    def test_is_upper(self):
        """Testeja si es majuscula."""
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """Testeja si es minuscula."""
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """Testeja si ho posa en majuscula."""
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()

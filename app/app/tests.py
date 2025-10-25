"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalsTests(SimpleTestCase):
    """Test the cal module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def tests_subtract_numbers(self):
        """Test subtract numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)

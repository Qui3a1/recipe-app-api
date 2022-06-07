"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    def tets_add_number(self):
        """test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
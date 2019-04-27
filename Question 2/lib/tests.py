import unittest
from .number_comparator import VersionComparator


class TestNumberComparator(unittest.TestCase):
    def test_greater_than(self):
        self.assertEqual(VersionComparator('1.1', '1.01').compare(), '"1.1” is greater than “1.01”.',
            'Should be greater than')

    def test_less_than(self):
        self.assertEqual(VersionComparator('1.3', '1.4').compare(), '"1.3” is less than “1.4”.',
            'Should be less than')


if __name__ == '__main__':
    unittest.main()

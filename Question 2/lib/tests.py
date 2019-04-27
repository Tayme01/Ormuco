import unittest
from .number_comparator import VersionComparator


class TestNumberComparator(unittest.TestCase):
    def test_greater_than(self):
        self.assertEqual(VersionComparator('1.1', '1.01').compare(), '"1.1” is greater than “1.01”.',
                         'Should be greater than')

    def test_less_than(self):
        self.assertEqual(VersionComparator('1.3', '1.4').compare(), '"1.3” is less than “1.4”.',
                         'Should be less than')

    def test_equal_to(self):
        self.assertEqual(VersionComparator('1.5', '1.5').compare(), '"1.5” is equal to “1.5”.',
                         'Should be equal to')

    def test_invalid_input_1(self):
        self.assertEqual(VersionComparator('a', '1.5').compare(), 'Invalid input passed! Check and try again.',
                         'Should be invalid')

    def test_invalid_input_2(self):
        self.assertEqual(VersionComparator('a').compare(), 'Invalid input passed! Check and try again.',
                         'Should be invalid')

    def test_invalid_input_3(self):
        self.assertEqual(VersionComparator().compare(), 'Invalid input passed! Check and try again.',
                         'Should be invalid')


if __name__ == '__main__':
    unittest.main()

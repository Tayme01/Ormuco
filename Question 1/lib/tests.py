import unittest
from .. import main


class TestNumberComparator(unittest.TestCase):
    def test_not_overlap(self):
        self.assertEqual(main.does_it_overlap('3 4', '5 7'), False, 'Should be False')

    def test_overlap(self):
        self.assertEqual(main.does_it_overlap('3 7', '4 8'), True, 'Should be True')

    def test_invalid_input(self):
        self.assertEqual(main.does_it_overlap(' ', '4 8'), 'Invalid input(s) passed! Check and try again.',
                         'Should be invalid input')

    def test_invalid_input_1(self):
        self.assertEqual(main.does_it_overlap(), 'Invalid input(s) passed! Check and try again.',
                         'Should be invalid input')

    def test_invalid_input_2(self):
        self.assertEqual(main.does_it_overlap('a b', 'b c'), 'Invalid input(s) passed! Check and try again.',
                         'Should be invalid input')


if __name__ == '__main__':
    unittest.main()

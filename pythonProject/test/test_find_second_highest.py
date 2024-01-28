import unittest

from src.Runnerupscore.util import find_second_highest

class MyTestCase(unittest.TestCase):
    def test_find_second_highest(self):
        n = 5
        arr = [3, 5, 5, 2, 4]

        res = find_second_highest(n, arr)
        actual = 4
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

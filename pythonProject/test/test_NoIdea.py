import unittest
from src.NoIdea.util import calculate_happiness


class MyTestCase(unittest.TestCase):
    def test_calculate_happiness(self):
        n, m = 3, 2
        arr = [1, 5, 3]
        set_A = {3, 1}
        set_B = {5, 7}
        res = calculate_happiness(n, m, arr, set_A, set_B)
        print(res)
        actual= 1
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

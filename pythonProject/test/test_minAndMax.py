import unittest
import numpy as np
from src.MinAndMax.util import minAndMax


class MyTestCase(unittest.TestCase):
    def test_minAndMax(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        res = minAndMax(data)
        print(res)
        actual= 7
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
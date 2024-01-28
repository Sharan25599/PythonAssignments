import unittest
from src.LinearAlgebra.util import calculate_rounded_determinant
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_calculate_rounded_determinant(self):
        my_matrix = np.array([[1, 2, -1], [3, 0, 4], [-2, 1, 5]])  # Sample matrix
        rounded_det = calculate_rounded_determinant(my_matrix)

        actual = -53.0
        self.assertEqual(rounded_det, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

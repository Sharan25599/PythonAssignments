import unittest
import numpy as np
from src.Floor_Ceil_Rint.util import calculate_floor_ceil_rint

class MyTestCase(unittest.TestCase):
    def test_floorceilrint(self):
        np.set_printoptions(legacy='1.13')
        my_numbers = [1.23, 4.56, 7.89, 10.11]
        floored, ceiled, rounded = calculate_floor_ceil_rint(my_numbers)
        actualFloor = np.array([  1.,   4.,   7.,  10.])
        actualCeil = np.array([  2.,   5.,   8.,  11.])
        actualRint = np.array([  1.,  5.,   8.,  10.])
        self.assertTrue(np.array_equal(floored, actualFloor))  # add assertion here
        self.assertTrue(np.array_equal(ceiled, actualCeil))  # add assertion here
        self.assertTrue(np.array_equal(rounded, actualRint)) # add assertion here


if __name__ == '__main__':
    unittest.main()

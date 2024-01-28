import unittest
from src.TimeDelta.util import time_delta

class MyTestCase(unittest.TestCase):
    def test_time_delta(self):
        res = time_delta("Fri 19 Jan 2024 04:35:00 +0530", "Fri 19 Jan 2024 05:12:45 +0530")
        print(res)

        actual = '2265'
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

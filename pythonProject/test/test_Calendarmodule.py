import unittest
from src.CalendarModule.util import find_day_of_week

class MyTestCase(unittest.TestCase):
    def test_find_day_of_week(self):
        res = find_day_of_week(11, 21, 2023)

        actual='TUESDAY'
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

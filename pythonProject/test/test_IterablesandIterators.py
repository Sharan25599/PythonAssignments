import unittest

from src.IterablesandIterators.util import at_least_one_a


class MyTestCase(unittest.TestCase):
    def test_at_least_one_a(self):
        n = 4
        letters = "a a c d".split()
        k = 2
        probability = at_least_one_a(n, letters, k)
        print(probability)
        actual=0.8333
        self.assertEqual(probability, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

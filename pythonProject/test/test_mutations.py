import unittest
from src.Mutations.util import insert_character


class MyTestCase(unittest.TestCase):
    def test_findingpercentage(self):
        string = "hello"
        character = "a"
        position = 3

        res = insert_character(string, character, position)
        print(res)
        actual = 'helalo'
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()


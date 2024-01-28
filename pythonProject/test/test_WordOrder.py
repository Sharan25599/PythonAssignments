import unittest


from src.WordOrder.util import count_word_occurrences

class MyTestCase(unittest.TestCase):
    def test_WordOrder(self):
        n = 4
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        res = count_word_occurrences(n, words)
        print(res)
        temp = ["3","2 1 1"]
        actual = "\n".join(map(str,temp))


        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

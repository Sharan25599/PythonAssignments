import unittest
from unittest.mock import patch
from io import StringIO  # Import StringIO correctly
from src.Floor_Ceil_Rint.util import merge_the_tools

class MyTestCase(unittest.TestCase):
    def test_mergethetool(self):
        s = "AABCAAADA"
        k = 3

        expected_output = ["AB", "CA", "AD"]

        with patch('sys.stdout', new=StringIO()) as captured_output:
            merge_the_tools(s, k)  # Call the function directly
            actual_output = captured_output.getvalue().strip().splitlines()

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()


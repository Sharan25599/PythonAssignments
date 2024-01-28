import unittest

from src.CollectionNamedTuple.util import calculate_average_marks_with_tuples


class MyTestCase(unittest.TestCase):
    def test_calculate_average_marks_with_tuples(self):
        num_students = 3
        column_names = ["ID", "NAME", "MARKS", "AGE"]
        student_data = [
            (1, "Alice", 85, 20),
            (2, "Bob", 90, 21),
            (3, "Charlie", 78, 22),
        ]

        average_marks = round(calculate_average_marks_with_tuples(num_students, column_names, student_data),2)

        actual= 84.33
        self.assertEqual(average_marks, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
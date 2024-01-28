from util import calculate_average_marks_with_tuples
num_students = 3
column_names = ["ID", "NAME", "MARKS", "AGE"]
student_data = [
    (1,"Alice", 85, 20),
    (2,"Bob", 90, 21),
    (3,"Charlie", 78, 22),
]

average_marks = calculate_average_marks_with_tuples(num_students, column_names, student_data)
print(f"Average marks: {average_marks:.2f}")
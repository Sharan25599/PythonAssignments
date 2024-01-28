def calculate_average_marks_with_tuples(num_students, column_names, student_data):

  marks_index = column_names.index("MARKS")
  marks_total = sum(float(student[marks_index]) for student in student_data)

  average_marks = marks_total / num_students
  return average_marks
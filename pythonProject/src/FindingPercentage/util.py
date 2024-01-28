
def findingpercentage(n,students,query_name):
    student_marks = {}
    for student_data in students:
        name, *scores = student_data.split()
        scores = list(map(float, scores))
        student_marks[name] = scores

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    return f"{avg:.2f}"


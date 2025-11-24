student = ["Bob", "Alex", "John", "Alan"]
marks = [23,76,65,43]

students_marks = dict(zip(student, marks))
for student,score in students_marks.items():
    print(student, score)
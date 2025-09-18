marks = [23,56,33,1,23,56,87,90,22,3,4,5,7,8,
1,23,44,56,78,90,14,16,78,77,66,33,22,76,98,0,9,34]
max_marks =marks[0]
for mark in marks:
    if mark > max_marks:
        max_marks = mark
print(max_marks)

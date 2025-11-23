names = ["Kibet", "Sam", "Ruth", "Angela","Rael","Jael","John"]
import random
student_scores={student:random.randint(20,80)
                for student in names}
passed = {student:score for (student, score)
                   in student_scores.items() if score > 50}

print(passed)
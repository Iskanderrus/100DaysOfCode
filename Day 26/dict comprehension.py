# בס״ד
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# make a dictionary from a list
students_scores = {key: random.randint(10, 101) for key in names}

print(students_scores)

# make a dictionary from an existing dictionary on a condition
passed_students = {key: value for (key, value) in students_scores.items() if value > 75}
print(passed_students)

# or just a list of passed students
print([key.upper() for (key, value) in students_scores.items() if value > 75])

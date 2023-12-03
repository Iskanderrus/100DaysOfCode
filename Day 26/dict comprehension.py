# בס״ד
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {key: random.randint(10, 101) for key in names}

print(students_scores)
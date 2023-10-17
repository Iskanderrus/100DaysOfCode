student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Nevill': 62
}
grades = dict()

for k, v in student_scores.items():
    if v >= 91:
        grades[k] = 'Outstanding'
    elif v >= 81:
        grades[k] = 'Exeeds Expectation'
    elif v >= 71:
        grades[k] = 'Acceptable'
    else:
        grades[k] = 'Fail'

print("\n".join(f"{k}: {v}" for k, v in grades.items()))

grade_groups = dict()

for k, v in grades.items():
    group = v
    if group in grade_groups:
        grade_groups[group].append(k)
    else:
        grade_groups[group] = [k]

print("\n".join(f"{k}: {v}" for k, v in grade_groups.items()))

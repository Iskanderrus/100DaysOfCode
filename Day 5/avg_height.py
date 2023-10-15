from math import ceil
from statistics import mean

student_heights = [180, 124, 165, 173, 189, 169, 146]

all_heights = 0
counter = 0

for height in student_heights:
    counter += 1
    all_heights += height

avg_height = ceil(all_heights / counter)
print(avg_height)

# option 2
print(ceil(mean(student_heights)))

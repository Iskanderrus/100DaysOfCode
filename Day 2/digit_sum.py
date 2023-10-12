# Write a script to sum all digits in the user whole number
number = input("What is your whole number?\n")
sum_numbers = sum([int(number[x]) for x in range(len(number))])
# or
# sum_numbers = 0
# for x in range(len(number)):
#    sum_numbers += int(number[x])
print(sum_numbers)

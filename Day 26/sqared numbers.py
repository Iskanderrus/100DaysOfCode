# בס״ד

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

result = [x for x in numbers if x % 2 == 0]
print(result)

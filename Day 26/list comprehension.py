# בס״ד

# Blueprint: new_list = [new_item] for item in list

numbers = range(1, 11)
squared_numbers = [x ** 2 for x in numbers]

# if condition in list comprehension
sqared_sqared_even_numbers = [y ** 2 for y in [x ** 2 for x in numbers] if y % 2 == 0]

print(squared_numbers)
print(sqared_sqared_even_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
print([name.upper() for name in names if len(name) > 5])

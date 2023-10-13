height = int(input('What is your height in cm?\n'))

if height >= 120:
    age = int(input('What is your age?\n'))
    if age >= 18:
        print("You are allowed to ride.\nYour ticket costs $12.00")
    elif age < 12:
        print("You are allowed to ride.\nYour ticket costs $5.00")
    else:
        print("You are allowed to ride.\nYour ticket costs $7.00")
else:
    print("You are not allowed to ride.")
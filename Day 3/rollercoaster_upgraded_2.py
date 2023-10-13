height = int(input('What is your height in cm?\n'))
ticket = 0

if height >= 120:
    age = int(input('What is your age?\n'))
    if age >= 18:
        ticket = 12
        print("You are allowed to ride.\nYour ticket costs $12.00")
    elif age < 12:
        ticket = 5
        print("You are allowed to ride.\nYour ticket costs $5.00")
    else:
        ticket = 7
        print("You are allowed to ride.\nYour ticket costs $7.00")
    photo = input('Do you need a photo? Y/N\n')
    if photo == 'Y':
        ticket_price = ticket + 3
        print(f'Your final price is ${float(ticket_price)}. Have Fun now!')
    else:
        print('No photo - no costs - no emotions...\nHave fun now!')
else:
    print("You are not allowed to ride.")
year = int(input('Which year do you want to check?\n'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('This year is leap.')
        else:
            print('This is not a leap year.')
    else:
        print('This year is leap.')
else:
    print('This is not a leap year.')

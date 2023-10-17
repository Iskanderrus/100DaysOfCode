n = int(input('Check this number: '))


def prime_checker(number):
    if number > 3:
        if number % 2 == 0 or number % 3 == 0:
            print('This is not a prime number')
        else:
            print('This is a prime number')
    elif number == 1:
        print('This is not a prime number')
    else:
        print('This is a prime number.')


prime_checker(number=n)

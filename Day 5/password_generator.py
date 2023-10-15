import string
from random import choice, shuffle

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)


def random_symbol_choice(list_of_symbols, number_of_symbols):
    random_symbols = []
    if number_of_symbols > 0:
        for x in range(number_of_symbols):
            random_symbols.append(choice(list_of_symbols))
        return random_symbols
    else:
        return random_symbols


def symbol_cleaning(initial_list, restricted_symbols_list):
    if len(restricted_symbols_list) > 0:
        for symbol in restricted_symbols_list:
            if symbol in initial_list:
                initial_list.remove(symbol)
    return initial_list


try:
    length = abs(int(input('How many symbols do you want in your password?\n')))
    upper_symbols = abs(int(input('How many upper case letters do you want in your password?\n')))
    digits = abs(int(input('How many digits should be in your password?\n')))
    num_symbols = abs(int(input('How many symbols do you want in your password?\n')))
    restricted_symbols = input("Please enter restricted symbols separated by space:\n")

    restricted_symbols = restricted_symbols.split(' ')
    print(restricted_symbols)

    if len(restricted_symbols) > 0:
        lower = symbol_cleaning(list(string.ascii_lowercase), restricted_symbols)
        upper = symbol_cleaning(list(string.ascii_uppercase), restricted_symbols)
        numbers = symbol_cleaning(list(string.digits), restricted_symbols)
        symbols = symbol_cleaning(list(string.punctuation), restricted_symbols)

    if length > 0 and length > (upper_symbols + digits + num_symbols):
        upper_list = random_symbol_choice(upper, upper_symbols)
        lower_list = random_symbol_choice(lower, (length - upper_symbols - digits - num_symbols))
        digit_list = random_symbol_choice(numbers, digits)
        symbol_list = random_symbol_choice(symbols, num_symbols)

        password_list = upper_list + lower_list + digit_list + symbol_list
        shuffle(password_list)

        password = ''.join(password_list)
        print(password)
    else:
        print('Some numbers mismatch. Please review your conditions.')

except ValueError:
    print('You entered not a valid number. Try again.')

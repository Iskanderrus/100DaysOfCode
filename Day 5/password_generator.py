import string
from random import choice, shuffle

# sets of symbols to use
lower = set(string.ascii_lowercase)
upper = set(string.ascii_uppercase)
numbers = set(string.digits)
symbols = set(string.punctuation)


def random_symbol_choice(set_of_symbols, num):
    """
    A function to select certain number of random elements from a collection of symbols.

    :param set_of_symbols: initial list of symbols to make a choice from
    :param num: number of symbols to be chosen
    :return: a list of randomly chosen symbols
    """
    return [choice(list(set_of_symbols)) for _ in range(num)]


try:
    # user entered values
    length = abs(int(input('How many symbols do you want in your password?\n')))
    num_of_upper_symbols = abs(int(input('How many upper case letters do you want in your password?\n')))
    num_of_digits = abs(int(input('How many digits should be in your password?\n')))
    num_of_symbols = abs(int(input('How many symbols do you want in your password?\n')))
    restricted_symbols = set(input('Please enter restricted symbols:\n'))
    recommended_symbols = set(input('Please enter recommended symbols:\n'))

    # cleaning collections of the symbols if there are restricted symbols
    if restricted_symbols and not recommended_symbols:
        lower = lower - restricted_symbols
        upper = upper - restricted_symbols
        numbers = numbers - restricted_symbols
        symbols = symbols - restricted_symbols

    # if there are recommended symbols, the collection of symbols will be limited to recommendations
    elif recommended_symbols:
        symbols = recommended_symbols

    # randomly select required number of symbols from each collection
    if length >= (num_of_upper_symbols + num_of_digits + num_of_symbols):
        upper_list = random_symbol_choice(upper, num_of_upper_symbols)
        lower_list = random_symbol_choice(lower, (length - num_of_upper_symbols - num_of_digits - num_of_symbols))
        digit_list = random_symbol_choice(numbers, num_of_digits)
        symbol_list = random_symbol_choice(symbols, num_of_symbols)

    # collecting and randomizing the final password
        password_list = upper_list + lower_list + digit_list + symbol_list
        shuffle(password_list)

        password = ''.join(password_list)
        print(password)
    else:
        print('Password length is not sufficient for the specified requirements.\nPlease review your conditions.')

except ValueError:
    print('You did not enter a valid number. Please try again.')

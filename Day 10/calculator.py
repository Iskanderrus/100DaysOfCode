"""
Simple calculator accepting whole and decimal numbers (both with comma and dot) and 4 basic operators.
Calculation result can be used in the next operation.
Or memory is cleared and new calculation performed.
Or user quits operation and exits the script.
"""


import os


def clear_screen():
    """
    A function to clear the screen when required. Works in Terminal only.
    """
    os.system('clear')


def sum_numbers(a, b):
    return a + b


def extract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None


def continue_check():
    """
    Function to check if calculation continues or must be stopped.
    :return: Answer defining if and how to continue.
    """
    while True:
        alert = input('If you want to continue with the result, type "yes"\n'
                      'If you want to continue with new numbers, type "no"\n'
                      'If you want to exit the app, type "quit"\n').lower().strip()
        if alert in ['yes', 'no', 'quit']:
            return alert
        else:
            print('Wrong input. Try again')


def input_request(previous_answer=None):
    """
    Function to request inputs from the user.
    If there is a result from the previous calculation, it is used as num_1 value.
    :param previous_answer: If there is a previous calculation and user choose to use it, it is being used.
    Otherwise, equals no None and both values are being prompted
    :return: Tuple containing two numbers (as floats) and operation sign (as string value)
    """
    try:
        if previous_answer is not None:
            num_1 = previous_answer
        else:
            num_1 = float(input('Please provide the first number:\n').replace(",", "."))
        operation = input('Please select operation:\n+\n-\n*\n/\n')
        num_2 = float(input('Please provide the second number:\n').replace(",", "."))
        return num_1, operation, num_2
    except ValueError:
        print('Please check inputs.')
        return input_request(previous_answer=previous_result)


make_calculations = True
previous_result = None

while make_calculations:
    num_a, action, num_b = input_request(previous_answer=previous_result)
    if action == '+':
        answer = sum_numbers(num_a, num_b)
    elif action == '-':
        answer = extract_numbers(num_a, num_b)
    elif action == '*':
        answer = multiply_numbers(num_a, num_b)
    elif action == '/':
        answer = divide_numbers(num_a, num_b)
        if answer is None:
            continue
    else:
        print("Invalid operation.")
        continue

    clear_screen()
    print(f'Correct answer is: {answer:.2f}')
    check_alert = continue_check()

    if check_alert == 'yes':
        previous_result = answer
    elif check_alert == 'no':
        previous_result = None
        clear_screen()
    elif check_alert == 'quit':
        clear_screen()
        make_calculations = False

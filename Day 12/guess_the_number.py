"""

Simple game where computer defines a number and user is prompted to guess it.
The game has two levels:
- easy - with 10 attempts to guess the correct number
- hard - with just 5 attempts to guess the correct number.

"""
from random import randint
from art import logo

# Number of attempts depending on the level difficulty
EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty_check():
    """
    Function to set the difficulty level depending on user's input. In case of a wrong input user is being requested to
    try again.
    :return: An integer defining the number of available attempts.
    """
    difficulty = input('Choose a difficulty level. Type "easy" or "hard": ').lower().strip()
    levels = {
        "easy": EASY_LEVEL,
        "hard": HARD_LEVEL,
    }

    if difficulty in levels.keys():
        return levels[difficulty]
    else:
        print('You typed not a valid respond. Try again.')
        return difficulty_check()


def comparison(num_1: int, num_2: int) -> str:
    """
    Function to compare the user input with the number selected by the computer.
    :param num_1: User input as integer.
    :param num_2: Computer selected number as integer.
    :return: A string value 'higher', 'lower' or 'match' to be used for further evaluation.
    """
    if num_1 > num_2:
        return 'higher'
    elif num_1 < num_2:
        return 'lower'
    else:
        return 'match'


def guess_game(attempts, target_number):
    while attempts > 0:
        print(f'\nYou have {attempts} {"attempts" if attempts != 1 else "attempt"} left.')

        try:
            user_guess = int(input('Make a guess: '))

        except ValueError:
            print('You didn\'t provide a valid number. You lose.')
            break

        else:
            compared = comparison(user_guess, target_number)
            if compared == 'match':
                print(f'Your guess {compared}. The correct number is {target_number}. You win!')
                attempts = 0
            else:
                attempts -= 1
                if attempts > 0:
                    print(f'Your number is {compared}. Try again.')
                else:
                    print(f'You are out of attempts. Targen number was {target_number}. You lose.')


if __name__ == '__main__':
    secret_number = randint(1, 100)
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking on a number between 1 and 100.")
    num_attempts = difficulty_check()
    guess_game(attempts=num_attempts, target_number=secret_number)

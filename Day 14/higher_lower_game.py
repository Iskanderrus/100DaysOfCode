import os
from random import choice
from game_data import data
from art import vs, logo


def clear_screen():
    """
    A function to clear the screen when required. Works in Terminal only.
    """
    os.system('clear')


def select_question(data_structure: list) -> dict:
    """
    Function to randomly select a dictionary with the question data from the dataset
    :param data_structure: Data set as list of dictionaries
    :return: A random dictionary from the list
    """
    question = choice(data_structure)
    return question


def play_again() -> bool:
    """
    A function to check if player wants to start the game again
    :return: True or False
    """
    question = input('\nWould you like to play again? y/n ').strip().lower()
    if question == 'y':
        return True
    elif question == 'n':
        return False
    else:
        print('Invalid input. Please enter either "y" or "n".')
        play_again()


def higher_lower_game(list_of_dictionaries, main_logo, vs_sign) -> None:
    """
    Main game function
    :return: None
    """
    clear_screen()
    person_1 = select_question(list_of_dictionaries)
    person_2 = select_question(list_of_dictionaries)
    score = 0
    # while loop till wrong answer
    while True:
        print(main_logo)
        # score is being printed only if more than 0
        if score > 0:
            print(f'\nYour score is: {score}')
        # main interface menu
        print(f"\nCompare A: {person_1['name'].strip().title()}, "
              f"who is {person_1['description'].strip()} "
              f"from {person_1['country'].strip().title()}.")
        print(vs_sign)
        print(f"Compare B: {person_2['name'].strip().title()}, "
              f"who is {person_2['description'].strip()} "
              f"from {person_2['country'].strip().title()}.")

        answer = input('Who has more followers? Type a or b: ').strip().lower()
        # main logic
        if ((answer == 'a' and person_1['follower_count'] > person_2['follower_count']) or
                (answer == 'b' and person_1['follower_count'] < person_2['follower_count'])):
            score += 1
            clear_screen()
            person_1 = person_2
            person_2 = select_question(list_of_dictionaries)

        else:
            message = f'\nSorry, but this is wrong. Your score is: {score}\n'
            print('*' * len(message))
            print(message)
            print('*' * len(message))
            break
    # after player has lost ask if he would like to start again
    continue_game = play_again()
    if continue_game:
        clear_screen()
        higher_lower_game(list_of_dictionaries=data, main_logo=logo, vs_sign=vs)
    else:
        clear_screen()
        message = 'Thank you for the game. See you soon again!'
        print(f"\n{'*' * len(message)}\n")
        print(message)
        print(f"\n{'*' * len(message)}\n")


higher_lower_game(list_of_dictionaries=data, main_logo=logo, vs_sign=vs)

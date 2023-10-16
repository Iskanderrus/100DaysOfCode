import string
from random import choice

lower = set(string.ascii_lowercase)
word_list = ['beekeeper', 'dwarf', 'railway', 'notebook', 'mouse', 'house', 'nurse']
counter = 0

word = choice(word_list)

substitute_list = ['_' for x in word]
substitute = ' '.join(substitute_list)
print(f'Word to guess is: {substitute}')
game_over = False
guessed_letters = set()


def find_indices(my_word, character):
    return [
        index for index, item in enumerate(my_word)
        if item == character
    ]


def letter_replacer(list_of_indexes, list_of_substitutes, letter):
    for index in list_of_indexes:
        list_of_substitutes[index] = letter
    return ' '.join(substitute_list)


def hangman_drawer(counter):
    stages = [
        '''
           -----
           |   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           o   |
               |
               |
        ''',
        '''
           -----
           |   |
           o   |
           |   |
               |
        ''',
        '''
           -----
           |   |
           o   |
          /|   |
               |
        ''',
        '''
           -----
           |   |
           o   |
          /|\\  |
               |
        ''',
        '''
           -----
           |   |
           o   |
          /|\\  |
          /    |
        ''',
        '''
           -----
           |   |
           o   |
          /|\\  |
          / \\  |
        '''
    ]
    print(stages[counter])


while '_' in substitute:
    if counter == 7:
        print('You have lost. The poor man is dead (((')
    letter = input('Guess a letter:\n').lower()

    if letter not in lower:
        print('This is not a valid letter')
        hangman_drawer(counter)
        counter += 1

    elif letter in guessed_letters:
        print('Do not repeat yourself.')
        hangman_drawer(counter)
        counter += 1

    elif letter not in word:
        print('You are wrong. This letter is not in our word.')
        hangman_drawer(counter)
        counter += 1

    else:
        indexes = find_indices(word, letter)
        substitute = letter_replacer(indexes, substitute_list, letter=letter)
        print(f"You are right.\n{substitute}")

    guessed_letters.add(letter)

print('You won!!! Congratulations!!!')




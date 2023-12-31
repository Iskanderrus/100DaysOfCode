# בס״ד

import zipfile
import pandas as pd
from io import StringIO

# reading data from zip archive without extracting
archive = zipfile.ZipFile('../../../Desktop/100 Days of Code The Complete Python Pro Bootcamp for 2023/26 - Day 26 - '
                          'Intermediate - List Comprehension and the NATO Alphabet/011 NATO-alphabet-start.zip', 'r')
raw_data = archive.read('NATO-alphabet-start/nato_phonetic_alphabet.csv')

# converting bites into the string
string_data = str(raw_data, 'utf-8')
data = StringIO(string_data)

# creating dataframe from the string object
df = pd.read_csv(data)
# print(df.head())

# creating a dictionary from the dataframe
spelling_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetics(dict_of_letters):
    # asking user for a word to spell
    user_input = input('What word do you want to spell?\n').strip().upper()
    # creating a list from the user input and the dictionary
    try:
        spelling = [f'{letter}: {dict_of_letters[letter]}' for letter in user_input]
    # if user input contains numbers or symbols:
    except KeyError:
        print('Sorry, only letters in the alphabet, please.\n')
        generate_phonetics(dict_of_letters)
    else:
        print(spelling)


generate_phonetics(spelling_dict)

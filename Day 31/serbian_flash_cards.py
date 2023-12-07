# בס״ד
"""
Preparing data
"""

from google.cloud import translate_v2 as translate
import pandas as pd

translate_client = translate.Client()

with open('data/sr_50k.txt', 'r') as file:
    data = file.readlines()

serbian = []
russian = []
for word in data:
    cleaned_word = word.split(' ')[0]
    serbian.append(cleaned_word)
    russian.append(translate_client.translate(word, target_language='ru', source_language='sr').lower())

df = pd.DataFrame([serbian, russian], columns=['Serbian', 'Russian'])
df.to_csv('./data/cleaned_words.csv')

# בס״ד
import string

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# counting length of each word and making a dictionary
result = {word.strip('?'): len(word) for word in sentence.split(' ')}

# finding only the words starting with upper case
upper_case_words = [word.strip('?') for word in sentence.split(' ') if word[0] in string.ascii_uppercase]

print(result)
print(upper_case_words)
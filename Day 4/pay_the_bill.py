"""

A script helping to decide who is going to pay the bill.

"""

from random import randint, choice

names = input('Give me everybody\'s names, separated by a comma.\n').split(',')

# solution 1
payer_index = randint(0, len(names) - 1)
print(f'Today {names[payer_index].strip().title()} is paying our bill.')

# solution 2
print(f'Or {choice(names).strip().title()} is paying the bill?')

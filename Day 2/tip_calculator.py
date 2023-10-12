# Build a simple tip calculator to count the bill for each person including tips.

print('Welcome to the tip calculator.')
bill = float(input('What is the total bill?\n').replace(',', '.'))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?\n').replace('%', ''))
people = int(input('How many people want to split the bill?\n'))
print(f"Each person should pay: ${round((bill + bill /100 * percentage) / people, 2)}")
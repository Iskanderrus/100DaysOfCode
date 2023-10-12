# Write a script calculating how many years, months and days remain till your 90th birthday
current_age = int(input('What is your current age in years?\n'))
max_age = 90

years = max_age - current_age
months = years * 12
weeks = years * 52
days = years * 365

print(f"You potentially could live {years} years or {months} months or {weeks} weeks or {days} days.\nIn days it looks much better...")
"""

The script to create the band name using users input of city and pet name

"""

print('Welcome to the Band Name Creator.')
city = input("What's name of the city you grew up in?\n").strip().title()
pet = input("What's your pet's name?\n").strip().title()
print(f"Your band name could be {city} {pet}")

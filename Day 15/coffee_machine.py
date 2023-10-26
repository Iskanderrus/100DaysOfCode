MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_request = input('What would you like (espresso/latte/capuccino)?\n').strip().lower()
if user_request == 'report':
    print(f'Water remained: {resources["water"]} ml.\n'
          f'Milk remained: {resources["milk"]} ml.\n'
          f'Coffee remained: {resources["coffee"]} gr.')
elif user_request == 'espresso':
    print(f"A cup of your favourite {user_request.title()} has price of ${MENU[user_request]['cost']}")
elif user_request == 'latte':
    print(f"A cup of your favourite {user_request.title()} has price of ${MENU[user_request]['cost']}")
elif user_request == 'capuccino':
    print(f"A cup of your favourite {user_request.title()} has price of ${MENU[user_request]['cost']}")
else:
    pass
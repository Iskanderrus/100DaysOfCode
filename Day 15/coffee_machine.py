import os
import sys
import time

SALES = 0
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
    "water": 45,
    "milk": 2000,
    "coffee": 500,
}

SOLD_DRINKS = {k: 0 for k in MENU.keys()}

BANK = {
    'quarters': 0,
    'dimes': 0,
    'nickles': 0,
    'pennies': 0,
}

failure_counter = {k: 0 for (k, v) in MENU.items()}


def reduce_resources(menu: dict, drink: str, resources_data: dict) -> dict:
    """
    Function to reduce the resources according to consumed ingredients
    :param menu: Dictionary containing drinks and required ingredients
    :param drink: Drink ordered by the customer
    :param resources_data: Dictionary containing currently available amounts of the ingredients
    :return: Updated dictionary containing currently available amounts of the ingredients
    """
    for ingredient in menu[drink]['ingredients']:
        resources_data[ingredient] -= menu[drink]['ingredients'][ingredient]
    return resources_data


def clear_screen():
    """
    A function to clear the screen when required. Works in Terminal only.
    """
    os.system('clear')


def resources_check(resources_dict: dict, menu_dict: dict, drink_name) -> bool:
    """
    Function to check if there is enough resources to make a selected drink based on the ingredients' requirement.
    :param resources_dict: Dictionary object containing all currently available resources to produce drinks.
    :param menu_dict: Dictionary object containing all drinks available on the menu and ingredients' requirements for
    each drink.
    :param drink_name: User selected drink name.
    :return: Boolean value: True if all ingredients are available, False if any of the ingredients is missing.
    If any ingredient is missing there is a service message being printed.
    """
    for resource in menu_dict[drink_name]['ingredients']:
        if resources_dict[resource] < menu_dict[drink_name]['ingredients'][resource]:
            print(f"We are out of {resource}.\n"
                  f"Please come again after 07:00 a.m. or 05:00 p.m. - our standard maintenance times.")
            return False
    return True


def report_call() -> None:
    """
    Service function to print report on remaining resources and lost sales for the service person.
    :return: None
    """
    global failure_counter, resources, SOLD_DRINKS, BANK
    clear_screen()
    print(f'Water remaining: {resources["water"]} ml.\n'
          f'Milk remaining: {resources["milk"]} ml.\n'
          f'Coffee remaining: {resources["coffee"]} gr.')
    for drink in failure_counter.keys():
        print(f"\nWe couldn't sell {failure_counter[drink]} cups of {drink} due to missing ingredients.")
    print()
    for coin in BANK.keys():
        print(f'{coin.title()}: {BANK[coin]}')
    print()
    for drink, value in SOLD_DRINKS.items():
        print(f'We sold {value} cups of {drink.title()}.')
    sales_report = f'\nTotal sales: {SALES}\n'
    print('*' * len(sales_report))
    print(sales_report)
    print('*' * len(sales_report))


def payment(menu, drink) -> float:
    global BANK
    price = menu[drink]['cost']
    print('Please insert coins.')
    paid_amount = 0.0
    while paid_amount < price:
        try:
            quarters = int(input('How many quarters? : '))
            dimes = int(input('How many dimes? : '))
            nickles = int(input('How many nickles? : '))
            pennies = int(input('How many pennies? : '))
        except ValueError:
            print('All inserted coins are returned.')
            print('Please, make sure to insert a valid coin.')
            payment(menu, drink)
        else:
            paid_amount += ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
            BANK['quarters'] += quarters
            BANK['dimes'] += dimes
            BANK['nickles'] += nickles
            BANK['pennies'] += pennies

            if paid_amount < price:
                print(f'Your {drink} costs ${price}.\n'
                      f'You paid ${paid_amount:.2f}.\n'
                      f'You still need to pay ${(price - paid_amount):.2f}')
    print(f'You paid ${paid_amount:.2f}')
    if paid_amount == price:
        print(f'Please enjoy your {drink}.')

    elif paid_amount > price:
        change = round((paid_amount - price), 2)
        change_in_quarters = change // 0.25
        rest_after_quarters = change % 0.25
        change_in_dimes = rest_after_quarters // 0.1
        rest_after_dimes = rest_after_quarters % 0.1
        change_in_nickles = rest_after_dimes // 0.05
        rest_after_nickles = rest_after_dimes % 0.1
        change_in_pennies = rest_after_nickles // 0.01

        BANK['quarters'] -= change_in_quarters
        BANK['dimes'] -= change_in_dimes
        BANK['nickles'] -= change_in_nickles
        BANK['pennies'] -= change_in_pennies

        print(f'Here is your change: ${change}')
        print(f'Please enjoy your {drink}.')

    return price


def quit_report():
    respond = input('To exit enter any value.\n')
    if respond:
        clear_screen()
        main_operation()


def main_operation():
    clear_screen()
    global SALES, MENU, failure_counter, resources
    if resources['water'] < 50 or resources['coffee'] < 18:
        print("I'm sorry. We are completely out of ingredients. Please come back later.")
    else:
        user_request = input('What would you like (espresso/latte/cappuccino)?\n').strip().lower()

        # calling a report for service
        if user_request == 'report':
            report_call()
            quit_report()

        # reset the coffee machine
        elif user_request == 'q':
            clear_screen()
            sys.exit()

        # customer service operation
        elif user_request in MENU.keys():
            if resources_check(resources, MENU, user_request):
                print(f"A cup of your favourite {user_request.title()} has price of ${MENU[user_request]['cost']}")
                resources = reduce_resources(MENU, user_request, resources)
                SOLD_DRINKS[user_request] += 1
                SALES += payment(menu=MENU, drink=user_request)
            else:
                failure_counter[user_request] += 1

        else:
            print('This drink is not in our menu. Please make a valid choice.')
        time.sleep(5)
        main_operation()


if __name__ == '__main__':
    main_operation()

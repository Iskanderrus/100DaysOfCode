# a script to calculate a pizza price depending on order parameters
print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L?\n').lower()
add_pepperoni = input('Do you want to add pepperoni? Y or N\n').lower()
extra_cheese = input('Do you want to have extra cheese? Y or N\n').lower()

final_price = 0

if extra_cheese == 'y':
    final_price += 1

if size == 's':
    final_price += 15
elif size == 'm':
    final_price += 20
elif size == 'l':
    final_price += 25

if add_pepperoni == 'y':
    if size == 's':
        final_price += 2
    else:
        final_price += 3
print(f'Your final bill is ${final_price}')

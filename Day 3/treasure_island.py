print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('\n\nWelcome to the Treasure Island.\nYour mission is to find the treasure.\n')
turn = input('You are on the crossing road. Where do you turn?\nType "left" or "right".\n').lower()
if turn == 'left':
    river = input('You reached a wide river. Would you wait for the boat or swim?\nType "wait" or "swim".\n').lower()
    if river == 'wait':
        door = input('You are in the castle in front of three doors. Red, yellow and blue. Which door would you '
                       'choose?\nType "red", "yellow" or "blue".\n').lower()
        if door == 'yellow':
            print('You won!')
        elif door == 'red':
            print('Wrong door - there was a dragon there. Game over')
        elif door == 'blue':
            print('Wrong door - there was a knight there. Game over')
    else:
        print('A huge alligator ate you. Game over')
else:
    print('There was a hole and you are trapped in it. Game over')

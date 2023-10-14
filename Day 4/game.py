from random import randint
import emoji

options = [":raised_fist:", ":victory_hand:", ":palm_down_hand:"]
computer_choice = randint(1, 3)

try:
    player_choice = int(input('Выбери: камень(1), ножницы(2) или бумага(3). \n'))

    if player_choice > 3 or player_choice < 1:
        print("Игрок ввёл неверный код. Компьютер выиграл...")
    elif player_choice == computer_choice:
        print(f"\nОба игрока выбрали {emoji.emojize(options[player_choice - 1])}.\nНичья!")
    elif ((player_choice == 1 and computer_choice == 2) or
          (player_choice == 2 and computer_choice == 3) or
          (player_choice == 3 and computer_choice == 1)):
        print("\nИгрок выбрал:")
        print(emoji.emojize(options[player_choice - 1]))
        print(f"Компьютер выбрал:")
        print(emoji.emojize(options[computer_choice - 1]))
        print("Выиграл игрок. Поздравляю!!!")
    else:
        print("\nИгрок выбрал:")
        print(emoji.emojize(options[player_choice - 1]))
        print(f"Компьютер выбрал:")
        print(emoji.emojize(options[computer_choice - 1]))
        print("Увы, в этот раз выиграл компьютер. Игрок проиграл...")
except ValueError:
    print("Игрок ввёл неверный код. Компьютер выиграл...")



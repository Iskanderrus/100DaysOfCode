from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_check(player_cards_tuple, computer_cards_tuple):
    if sum(player_cards_tuple) == 21:
        print('Blackjack! You win!')
        return continue_game()
    elif sum(player_cards_tuple) > 21:
        print('You are over 21. You lose :-(')
        return continue_game()

    else:



def draw_card(cards_list: list) -> int:
    return choice(cards_list)


def initial_draw(card_list):
    player_cards = (draw_card(cards_list=card_list), draw_card(cards_list=card_list))
    computer_cards = (draw_card(cards_list=card_list), draw_card(cards_list=card_list))
    return player_cards, computer_cards


def continue_game():
    check = input('Do you want to continue the game? "y" or "n"\n')
    if check == 'y':
        return True
    elif check == 'n':
        return False
    else:
        print('Please check your answer.')
        continue_game()

initial_draw_cards = initial_draw(cards)

player_initial_draw = initial_draw_cards[0]
computer_initial_draw = initial_draw_cards[1]


print(f'Your cards are: {player_initial_draw}')
print(f"Computer's first card is: {computer_initial_draw[0]}")



draw_check = input("If you want to draw, type 'y'\nIf you want to pass, type 'n'\n")
    if draw_check == 'y':
        new_player_card = draw_card(cards)
        player_initial_draw = (*player_initial_draw, new_player_card)
        total_player_sum = sum(player_initial_draw) + new_player_card
        print(f"Your next card is: {new_player_card}")
        print(f" Your cards are: {player_initial_draw}")

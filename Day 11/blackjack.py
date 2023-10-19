from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True


def sum_check(player_cards_list, computer_cards_list):
    if sum(computer_cards_list) < 17:
        computer_cards_list.append(draw_card(cards))
    elif sum(player_cards_list) == sum(computer_cards_list) == 21:
        print('Draw!')
        return continue_game()
    elif sum(player_cards_list) == 21:
        print('Blackjack! You win!')
        return continue_game()
    elif sum(player_cards_list) > 21:
        print('You are over 21. You lose :-(')
        return continue_game()
    elif sum(computer_cards_list) == 21:
        print(f'Computer has {sum(computer_cards_list)}. You lose :-(')
        return continue_game()
    else:
        # If none of the above conditions are met, return False to indicate the game should not continue
        return False


def draw_card(cards_list: list) -> int:
    return choice(cards_list)


def initial_draw(card_list):
    player_cards = [draw_card(cards_list=card_list), draw_card(cards_list=card_list)]
    computer_cards = [draw_card(cards_list=card_list), draw_card(cards_list=card_list)]
    results = [player_cards, computer_cards]
    return results


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
while game_on:
    game_on = sum_check(player_initial_draw, computer_initial_draw)
    initial_draw_cards = initial_draw(cards)

    player_initial_draw = initial_draw_cards[0]
    computer_initial_draw = initial_draw_cards[1]
    print(f'Your cards are: {player_initial_draw}')
    print(f"Computer's first card is: {computer_initial_draw[0]}")

    # draw_check = input("If you want to draw, type 'y'\nIf you want to pass, type 'n'\n")
    # if draw_check == 'y':
    #     new_player_card = draw_card(cards)
    #     player_initial_draw.append(new_player_card)
    #     total_player_sum = sum(player_initial_draw)
    #     print(f"Your next card is: {new_player_card}")
    #     print(f" Your cards are: {player_initial_draw}")
    #     game_on = sum_check(player_initial_draw, computer_initial_draw)

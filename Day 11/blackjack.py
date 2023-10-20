from random import choice
import os
import emoji


def clear_screen():
    """
    A function to clear the screen when required. Works in Terminal only.
    """
    os.system('clear')


def calculate_score(cards_list: list) -> int:
    """
    Function to calculate the score.
    :param cards_list: List of the integers after the draw
    :return: Total sum of the cards as an integer or 0 if player has Blackjack
    """
    score = sum(cards_list)
    if len(cards_list) == 2 and score == 21:
        return 0
    elif score > 21 and 11 in cards_list:
        cards_list = [1 if x == 11 else x for x in cards_list]
    return sum(cards_list)


def draw_card(cards_list: list) -> int:
    """
    Return random card from the deck.
    :param cards_list: List with all cards available
    :return: Card as integer
    """
    return choice(cards_list)


def compare_score(player_score_list, computer_score_list):
    if player_score_list == computer_score_list:
        return "Draw!"
    elif computer_score_list == 0:
        return (f"Lose, opponent has Blackjack... "
                f"{emoji.emojize(':squinting_face_with_tongue:')}"
                f"{emoji.emojize(':crying_face:')}")
    elif player_score_list == 0:
        return (f"Win with a Blackjack! "
                f"{emoji.emojize(':smiling_face_with_sunglasses:')}"
                f"{emoji.emojize(':star-struck:')}")
    elif player_score_list > 21:
        return f"You went over. You lose... {emoji.emojize(':crying_face:')}"
    elif computer_score_list > 21:
        return f"Opponent went over. You win! {emoji.emojize(':smiling_face_with_sunglasses:')}"
    elif player_score_list > computer_score_list:
        return f"You win! {emoji.emojize(':smiling_face_with_sunglasses:')}"
    else:
        return "You lose..."


def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_on = True
    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(draw_card(cards))
        computer_cards.append(draw_card(cards))
    player_score = 0
    computer_score = 0

    while game_on:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print('Player cards ', player_cards)
        print('Player score ', player_score)
        print('Computer\'s card ', computer_cards[0])
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_on = False
        else:
            player_should_deal = input('Type "yes" to get another card, type "n" to pass: ')
            if player_should_deal.strip().lower() == 'y':
                player_cards.append(draw_card(cards))
                clear_screen()
            else:
                game_on = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card(cards))
        computer_score = calculate_score(computer_cards)

    clear_screen()
    print(f'\t Your final hand: \t\t{player_cards}\n\t Your final score: \t\t{player_score}\n\n')
    print(f'\t Computer\'s final hand: \t{computer_cards}\n\t Computer\'s final score: \t{computer_score}\n')
    print(compare_score(player_score_list=player_score, computer_score_list=computer_score))


while input('Do you want to play BlackJack? If yes, type "y" ').strip().lower() == 'y':
    clear_screen()
    play_blackjack()
clear_screen()

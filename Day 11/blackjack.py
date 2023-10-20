from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True


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


def compare_score(player_score, computer_score):
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack..."
    elif player_score == 0:
        return "Win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose..."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose..."


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
        else:
            game_on = False

while computer_score != 0 and computer_score < 17:
    computer_cards.append(draw_card(cards))
    computer_score = calculate_score(computer_cards)

print(compare_score(player_score=player_score, computer_score=computer_score))

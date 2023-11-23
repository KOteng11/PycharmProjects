from art import logo
import random


def calculate_score(hands):
    """Take a list of cards and return the score calculated from the card"""
    if sum(hands) == 21 and (len(hands) == 2):
        return 0
    if 11 in hands and sum(hands) > 21:
        hands.remove(11)
        hands.append(1)
    return sum(hands)


def draw_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "You lose, opponent has a Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"


def play_game():

    print(logo)
    player_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        player_hand.append(draw_card())
        computer_hand.append(draw_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"\tYour cards: {player_hand}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                player_hand.append(draw_card())
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_hand.append(draw_card())
            computer_score = calculate_score(computer_hand)

        print(f"\tYour final cards: {player_hand}, current score: {player_score}")
        print(f"\tComputer's final cards: {player_hand}, current score: {player_score}")
        print(compare(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == 'y':
    play_game()
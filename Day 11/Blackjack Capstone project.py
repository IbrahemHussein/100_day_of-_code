############### Blackjack Project #####################
# import library
import random
from art import logo
import sys
import os


# Hint : Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """return a random card fron the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Hint : Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21,
# then the user loses. If the computer_score is over 21, then the computer loses. If none of the above,
# then the player with the highest score wins.


def compare(user_score, computer_score):
    """take the value of the user and computer and compare them and then return the winner """
    if user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif computer_score == user_score:
        return "Draw 🙃"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif user_score > computer_score:
        return 'you  win 😁'
    else:
        return 'you lose 😤 '

# Hint : Create a function called calculate_score() that takes a List of cards as input
# and returns the score. Look up the sum() function to help you do this.


def calculator(card):
    """take a list of cards and return the score calculated from the cards"""
    # Hint : Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(card) == 21 and len(card) == 2:
        return 0

    # Hint : Inside calculate_score() check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1. You might need to look up append() and remove().

    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def play_game():
    """ to start game """
    print(logo)
    Is_game_over = False
   # Hint : Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint : Call calculate_score(). If the computer or the user has a blackjack (0)
    #  or if the user's score is over 21, then the game ends.
    # loop for user iteration
    while not Is_game_over:
        user_score = calculator(user_cards)
        computer_score = calculator(computer_cards)
        print(f'your cards: {user_cards},current score {user_score}')
        print(f'computer  first card: {computer_cards[0]}')
        # Hint 10: If the game has not ended, ask the user if they want to draw another card.
        # If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            Is_game_over = True
        else:
            user_should_deal = input(
                'Type "y" to get anther card,type "n" to pass : ')
            if user_should_deal == '':
                print('look like you forget to enter a value ')
                user_should_deal = input(
                    'Type "y" to get anther card,type "n" to pass : ')
            else:
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                elif user_should_deal == 'n':
                    Is_game_over = True
                else:
                    print('sorry ,you have enter a wrong value ')
                    user_should_deal = input(
                        'Type "y" to get anther card,type "n" to pass : ')

    # Hint : Once the user is done, it's time to let the computer play.
    #  The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculator(computer_cards)
    print(f'your final hand : {user_cards} ,finial score : {user_score}')
    print(
        f'computer final hand : {computer_cards} ,finial score : {computer_score}')
    print(compare(user_score, computer_score))

# Hint 14: Ask the user if they want to restart the game. If they answer yes,
#  clear the console and start a new game of blackjack and show the logo from art.py.


while input('Do you went to play a game of blackjact? type "y" or to end  type "no"') == 'y':
    os.system('cls')
    play_game()

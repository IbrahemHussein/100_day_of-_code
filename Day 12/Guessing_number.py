import random
import os
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# function to chack user's guess against actual answer


def chack_answer(guess, answer, turns):
    ''' chack if the guess equal the answer or not  and return turns'''
    if guess > answer:
        print(' your guess Too hight ')
        return turns - 1
    elif guess < answer:
        print('your guess Too low ')
        return turns - 1
    else:
        print(f'tou got it ! the answer was {answer}')
# Make a function to set a diffeculty


def set_difficulty():
    """to chose the level of game """
    level = input('choose a difficulty . Type "easy" or "hard" : ')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    ''' run to start game '''

    # choosing a random number between 1 and 100
    answer = random.randint(1, 100)
    print(logo)
    print("welcom to the Number Gussing Game !\n I'm thinking of a number between 1 and 100")
    print(f'passt,the corrent answer is {answer}')

    turns = set_difficulty()

    # Repeat the guessing functionlity if they get it wrong
    guess = 0
    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the number ')
        # let the user guess a number
        guess = int(input('Make a guess: '))
        turns = chack_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses ,you lose")
            return
        elif guess != answer:
            print('Guess again')
    paly_again = input(
        'hi again if ypu went to play again type "y" or to  exit type "n" :')
    if paly_again == 'y':
        os.system('cls')
        game()
    else:
        print('see you again ')


game()

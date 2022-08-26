from art import logo, vs
from game_data import data
import os
# import random library
import random


def random_choce(data):
    """function to generate a random account from game data"""
    return random.choice(data)


def descrption(account):
    """function to format that account data into printable formate """
    name = account['name']
    follower = account['follower_count']
    description = account['description']
    country = account['country']
    return f'{name} ,{description}, from : {country}'


def chock_answer(user_chose, accountA, accountB):
    ''' Take a user guess and followers and return if they got it right '''
    if accountA > accountB:
        return user_chose == 'a'
    elif accountB > accountA:
        return user_chose == 'b'


def start_game():
    '''function to start a game '''
    acountA = random_choce(data)
    acountB = random_choce(data)

    # Display art
    print(logo)
    Score = 0
    game_continue = True
    while game_continue:
        acountA = acountB
        acountB = random_choce(data)
        while acountA == acountB:
            acountB = random_choce(data)
        print('Compare A:', descrption(acountA))
        print(vs)
        print('Against B:', descrption(acountB))
        # Ask user for a guess
        user_chose = input('Who has more followers? "A" or "B" :').lower()
        # Get followers count of each account
        a_followes_count = acountA['follower_count']
        b_fllowers_count = acountB['follower_count']
        # Chack if user correct
        is_correct = chock_answer(
            user_chose, a_followes_count, b_fllowers_count)
        # keep score
        if is_correct:
            Score += 1
            # Clear the screen between round
            os.system('cls')
            print(f"You're right ! Currect score : {Score}")

        else:
            print(f"Sorry,that's wrong.Final Score : {Score}")
            game_continue = False


start_game()

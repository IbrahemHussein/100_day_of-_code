from turtle import clear
from art import logo
print(logo)

def find_hight_bidder(bidding_recored):
    highest_bid=0
    for bidder in bidding_recored:
        bid_amount=bidding_recored[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'the winner is {winner} with a bid of ${highest_bid}')

bids={}
bidding_finshed=False
while not bidding_finshed:
    name=input('what is yoour name? : ')
    price=int(input('what is your bid? : $'))
    bids[name]=price
    should_continue=input('Are there any other bidder? Types "yes" or "no"').lower()
    if should_continue == 'no':
        bidding_finshed=True
        find_hight_bidder(bids)
    

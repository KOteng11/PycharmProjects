import os
from art import logo


def clear():
    os.system('cls')


def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""

    for bidder in bidding_records:
        amount = bidding_records[bidder]

        if amount > highest_bid:
            highest_bid = amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_biding = True

bidding_details = []
bids = {}

while continue_biding:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bids[name] = price
    bidding_details.append(bids)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        continue_biding = False

highest_bidder(bids)



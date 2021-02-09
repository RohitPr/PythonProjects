from art import logo
from os import system

print(logo)
print("Welcome to the secret Auction Program")

bidders = True

while bidders:
    name = input('\nWhat is your name : ')
    bid = int(input("\nWhat is your bid : Rs "))
    bidders = input("\nAre there any other bidders? Type 'Yes' or 'No' : ")

    secret_bid = {}
    secret_bid[name] = bid

    def bidding_record(secret_bid):
        highest_bid = 0
        winner = ""
        for bidder in secret_bid:
            bid_amount = secret_bid[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"\nThe winner is {winner} with highest bid of Rs {highest_bid}")

    if bidders == 'No':
        bidders = False
        bidding_record(secret_bid)

    else:
        system('cls')

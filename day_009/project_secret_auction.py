import os


from art import logo
print(logo)
print("Welcome to the secret auction program.")

bidding_complete = False
total_bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the auction is {winner}. They won with a bid of ${highest_bid}.")
    
while not bidding_complete:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    total_bids[name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if more_bids == "no":
        bidding_complete = True
        find_highest_bidder(total_bids)
    elif more_bids == "yes":
        os.system('clear')






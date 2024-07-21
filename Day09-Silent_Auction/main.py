from replit import clear
import os
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

#create dictionary
# each name is a key
# the value is their bid
# at the end loop through dictionary and find the person who made the highest bid

additional_bidders = True
bidding_dict = {}
while additional_bidders == True:
    bidder_name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bidding_dict[bidder_name]= bid

    continue_auction = input("Are there additional bidders? Type 'yes' or 'no'.")

    if continue_auction != 'yes':
        additional_bidders = False
    elif continue_auction == 'yes':
        clear()

starting_bidder = list(bidding_dict.keys())[0]
starting_bid = list(bidding_dict.values())[0]

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winner of the action is {highest_bidder} with a bid of ${highest_bid}.")

find_highest_bidder(bidding_dict)


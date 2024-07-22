############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Import Libraries
import random
from replit import clear
from art import logo
import numpy as np


## Create Functions
def deal_card():
    """Will deal one additional card randomly from an infinite deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def deal_first_hand():
    """To start the game. Deals the user and computer 2 cards using the deal_card() function.
    Output is 2 lists: user_cards, computer_cards"""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    return user_cards, computer_cards
def calculate_score(card_list):
    """Will calculate the score given the current hand"""
    score = np.sum(card_list)
    #Check for blackjack in the beginning. This is when you have 2 cards and have 21
    if len(card_list) == 2 & score == 21:
        return 0
    #In Blackjack an ace can count as 1 or 11. If we've gone over, replace the 11 with a 1
    if 11 in card_list and np.sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
        return np.sum(card_list)
    else:
        return np.sum(card_list)
def compare(user_score, computer_score):
    """Function to compare the final scores once the game is over.
    Output is a print statement that tells the user the result of the game"""
    if user_score > 21:
        return "You lose, you went over"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > computer_score:
        return "You win."
    elif computer_score > user_score:
        return "You lose."




def play_blackjack():
    """Code for the steps of playing the blackjack game. Will allow user to play blackjack against a computer"""
    print(logo)
    #Set a flag so that the game ends when certain conditions are met
    is_game_over = False
    user_cards, computer_cards = deal_first_hand()

    #The user while loop. Will allow the user to take more cards, as long as the game hasn't ended
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    computer_score = calculate_score(computer_cards)
    #Computer while loop: Allows the computer to draw more cards if their current score is < 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    #When the game has ended print the final results!
    print(f"Your final hand is {user_cards}, final score is {np.sum(user_cards)}")
    print(f"The Computer's final hand is {computer_cards}, their final score is {np.sum(computer_cards)}")
    print(compare(user_score, computer_score))
# While loop to allow the user to play multiple games of blackjack
while input("Would you like to play a game of Blackjack? 'y' or 'n' ") == 'y':
    clear()
    play_blackjack()
print("Thanks for Playing!")








#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Ask user to guess a number. Check if that number matchs. Return if the guess is too low or too high
def check_answer(guess, answer, turns):
    """Checks answer against guess and returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    if guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        return turns

#function to set difficulty
def set_difficulty():
    """Ask user for difficulty level and return the appropriate number of attempts"""
    difficulty_level = input("Chose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def number_game():
    print(logo)
    # intro to the program. Welcome. Thinking of number. Chose difficulty level
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")

    #generate a random number between 1 and 100.
    answer = randint(1, 100)
    # print(answer)
    turns = set_difficulty()

    #declare the variable outside of the while loop so that its defined
    user_guess = 0
    while (user_guess != answer) & (turns >= 1):
        print(f"You have {turns} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))

        #update the local variable everytime we check the guess against the answer

        turns = check_answer(user_guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose.")
            # with functions you can write returns to exit and end the function
            return
        elif (user_guess != answer) & (turns >= 1):
            print("Guess Again!")




number_game()

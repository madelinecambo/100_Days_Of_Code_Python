#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print(logo)

# intro to the program. Welcome. Thinking of number. Chose difficulty level
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")

#generate a random number between 1 and 100.
random_number = random.randint(1, 100)

#if statement that instatiates guesses based on difficult level. 10 for easy, 5 for hard
difficulty_level = input("Chose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == 'hard':
    attempts_left = 5
else:
    attempts_left = 10

# create a flag that will be used in a while loop to allow the user to guess multiple times
game_over = False

while not game_over:
    print(f"You have {attempts_left} attempts remaining to guess the number")
    #Ask user to guess a number. Check if that number matchs. Return if the guess is too low or too high
    user_guess = int(input("Make a guess: "))
    #increment the attempts down by 1. Tell user to guess again. Repeat process until attempts are out. or user guesses correctly
    if (user_guess == random_number) & (attempts_left > 1):
        print(f"You got it! The answer was {random_number}")
        game_over = True
    elif (user_guess != random_number) & (attempts_left == 1):
        print("You've run out of guesses. You lose.")
        game_over = True
    elif user_guess < random_number:
        print("Too low.\nGuess Again")
        attempts_left -= 1
    elif user_guess > random_number:
        print("Too high.\nGuess Again")
        attempts_left -= 1


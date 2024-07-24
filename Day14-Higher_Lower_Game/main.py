from art import logo, vs
from game_data import data
from random import shuffle
import numpy as np

print(logo)

index = 0
score = 0
game_over = False
shuffle(data)


def generate_more_data(data):
    """A function to return a new shuffled dataset to append to the end if user runs of people to compare"""
    new_data = data.copy()
    shuffle(new_data)
    return new_data

def make_comparison_game(starting_index):
    """A function to iteration through the list of people we have to compare instagram followers.
    Returns the first and second people and the index of the starting person"""
    person_a = data[starting_index]
    person_b = data[starting_index + 1]
    return(person_a, person_b, starting_index)

def show_comparison(person_a, person_b):
    """To show the user Person A vs Person B and allow them to guess which has more instagram followers"""
    print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, {person_b['description']}, from {person_b['country']}.")

def check_user_guess(person_a, person_b, user_guess, score):
    """For checking if the user guessed correctly or incorrectly.
    Game ends if they were not correct and final score is shown.
    Function returns the final score, and if the game is over or not"""
    highest_follower_count = np.max([person_a['follower_count'], person_b['follower_count']])
    if user_guess == 'a':
        guessed_follower_count = person_a['follower_count']
    elif user_guess == 'b':
        guessed_follower_count = person_b['follower_count']
    else:
        print(f"You guessed incorrectly. Final score: {score}")
        return score, True
    if guessed_follower_count == highest_follower_count:
        score += 1
        print(f"You're Right! Current score: {score}")
        return score, False
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return score, True

def comparision_game(game_over, index, score):
    """A function for running the comparison game.
    Includes a section for generating more data, if the user runs out.
    As long as the user guesses correctly the game will continue."""
    while not game_over:
        # if the indexes get to the end, generate more data by adding on a shuffled list
        if index >= len(data) - 2:
            new_data = generate_more_data(data)
            for person in new_data:
                data.append(person)

        person_a, person_b, next_index = make_comparison_game(index)
        index += 1
        show_comparison(person_a, person_b)
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        score, game_over = check_user_guess(person_a, person_b, user_guess, score)

    return game_over, index, score

continue_game = True
while continue_game:
    # persist the game_over, index, and score from round to round
    game_over, index, score = comparision_game(game_over, index, score)

    #if player loses, ask them if they'd like to continue. Pick up where they left off.
    if input("Continue the game from where you left off? 'Y' or 'N' :").lower() == 'y':
        continue_game = True
        game_over = False
    else:
        continue_game = False













#


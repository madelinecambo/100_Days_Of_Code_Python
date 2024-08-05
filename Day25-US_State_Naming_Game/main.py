import turtle
import pandas as pd
from correct_answer import CorrectAnswer

# Read in the States and their map coordinates
state_coordinates = pd.read_csv("50_states.csv")

# Create the screen object
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_correctly = []
all_states = state_coordinates.state.tolist()

while len(guessed_correctly) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_correctly)}/50 States Correct", prompt= "What's another State's name?").title()
    if answer_state == "Exit":
        # create empty list to hold the states that were missed
        missing_states = []
        # loop through every state. Append it to the missing states if it was not guessed
        for state in all_states:
            if state in guessed_correctly:
                pass
            else:
                missing_states.append(state)
        # create dataframe from the list of missing states
        states_to_learn= pd.DataFrame(missing_states)
        # write data to csv
        states_to_learn.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        state = answer_state
        x = state_coordinates[state_coordinates['state'] == state]['x'].item()
        y = state_coordinates[state_coordinates['state'] == state]['y'].item()
        # create and object from the CorrectAnswer class to write the correct answer on the Map
        correct = CorrectAnswer(x, y, state)
        # append the correct answer to the list
        guessed_correctly.append(state)

screen.exitonclick()
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

while len(guessed_correctly) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_correctly)}/50 States Correct", prompt= "What's another State's name?").title()

    if answer_state in state_coordinates.state.tolist():
        state = answer_state
        x = state_coordinates[state_coordinates['state'] == state]['x'].values[0]
        y = state_coordinates[state_coordinates['state'] == state]['y'].values[0]
        correct = CorrectAnswer(x, y, state)

        guessed_correctly.append(state)

screen.exitonclick()
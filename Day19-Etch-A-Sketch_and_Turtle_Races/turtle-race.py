from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
starting_y = -120

for turtle in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle)
    new_turtle.penup()
    new_turtle.goto(x = -230, y = starting_y)
    starting_y += 50
    # a list of turtle instances where they all have a different state
    all_turtles.append(new_turtle)


# use the go to method which allows us to give an x and y value

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()


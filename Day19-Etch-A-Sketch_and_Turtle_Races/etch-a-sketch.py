from turtle import Turtle, Screen

# create Tim, a turtle object
tim = Turtle()
screen = Screen()


# Challenge - Build an Etch-A-Sketch
# W = forwards
# S = Backwards
# A = counter-clockwise
# D = clockwise
# C = clear


# The on key function can only receive a function with no arguments
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    tim.left(-10)

def move_clockwise():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# updated the binding from space to w
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = move_counterclockwise)
screen.onkey(key = "d", fun = move_clockwise)
screen.onkey(key = "c", fun = clear)

screen.exitonclick()
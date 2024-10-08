from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(starting_pos)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




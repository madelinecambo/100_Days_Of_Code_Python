from turtle import Turtle
FONT = ("Courier", 12, "normal")

class CorrectAnswer(Turtle):
    def __init__(self, x_cor, y_cor, state_name):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(f"{state_name}", align="center", font=FONT)
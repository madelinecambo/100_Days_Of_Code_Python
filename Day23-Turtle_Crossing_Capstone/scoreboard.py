from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 265)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

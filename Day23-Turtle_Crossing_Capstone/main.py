import time
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Initialize Turtle Player
player = Player()
scoreboard = ScoreBoard()
scoreboard.update_scoreboard()
car_manager = CarManager()

# Set Screen to listen for player keystrokes
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(level=scoreboard.level)

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player is at finish line
    if player.is_at_finish_line():
        player.reset_player()
        scoreboard.increment_level()
        scoreboard.update_scoreboard()

screen.exitonclick()

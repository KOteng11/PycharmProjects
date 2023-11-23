import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

for _ in range(3):
    car = CarManager()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkeypress(player.move_up, "Up")

    if player.ycor() > 300:
        player.reset_position()
        scoreboard.update_level()

    # creates a car
    # car.create_car()
    car.move_car()
screen.exitonclick()

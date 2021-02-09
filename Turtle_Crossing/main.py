from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Level

import time

screen = Screen()
screen.setup(width=700, height=650)
screen.title("Turtle Crossing")
screen.bgcolor("gray")
screen.tracer(0)

player = Player()
car = Cars()
level = Level()

screen.listen()
screen.onkey(player.move, "w")

game = True
while game:
    screen.update()
    time.sleep(1)
    car.generate_cars()

    # Detect Collision with Cars
    for all in car.cars_list:
        if all.distance(player) < 20:
            level.game_over()
            game = False

    # Level Crossed
    if player.ycor() > 300:
        time.sleep(1)
        level.update_level()
        car.next_level()
        player.reset_position()

screen.exitonclick()

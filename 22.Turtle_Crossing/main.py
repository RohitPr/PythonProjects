from turtle import Screen
from player import Player
from cars import Car
from level import Level
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.title("Turtle Crossing")
screen.bgcolor("gray")
screen.tracer(0)

player = Player()
car = Car()
level = Level()

screen.listen()
screen.onkey(fun=player.up, key="w")

game = True

while game:
    screen.update()
    time.sleep(1)
    car.create_cars()

    # Detect Level Change
    if player.ycor() > 280:
        level.update_level()
        player.reset_position()
        car.next_level()

    # Detect Car Collision with Player
    for a in car.all_cars:
        if a.distance(player) < 15:
            level.game_over()
            game = False

screen.exitonclick()

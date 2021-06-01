from turtle import Turtle, Screen
import random

COLORS = ("red", "yellow", "green", "blue", "pink", "orange")

screen = Screen()
screen.title("Turtle")
screen.screensize(canvwidth=500, canvheight=400)

tur = Turtle()

a = 0

while a < 36:
    tur.speed(0)
    tur.hideturtle()
    screen.bgcolor(random.choice(COLORS))
    tur.color(random.choice(COLORS))
    tur.circle(radius=100)
    tur.tilt(angle=10)
    tur.left(10)
    a += 1

screen.bgcolor("white")
screen.exitonclick()
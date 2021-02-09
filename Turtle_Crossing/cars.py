from turtle import Turtle
import random

LOCATION = [(300, 0), (300, -40), (300, -80), (300, -120), (300, -160), (300, -200),
            (300, 40), (300, 80), (300, 120), (300, 160), (300, 200), (300, 240)]

COLORS = ["yellow", "blue", "pink", "green", "red", "orange", "black"]

MOVE = 20

class Cars():
    def __init__(self):
        self.cars_list = []
        self.speed = 0

    def generate_cars(self):
        tur = Turtle()
        tur.shape("square")
        tur.hideturtle()
        tur.penup()
        tur.setheading(180)
        tur.shapesize(stretch_wid=1, stretch_len=3)
        tur.showturtle()
        tur.color(random.choice(COLORS))
        tur.goto(random.choice(LOCATION))
        self.cars_list.append(tur)
        self.cars_move()

    def cars_move(self):
        for a in self.cars_list:
            a.forward(MOVE + self.speed)

    def next_level(self):
        self.speed += 5

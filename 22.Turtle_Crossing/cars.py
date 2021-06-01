from turtle import Turtle
import random

POSITION = [(300, 0), (300, 40), (300, 80), (300, 120), (300, 160), (300, 200),
            (300, -40), (300, -80), (300, -120), (300, -160), (300, -200)]

COLORS = ("red", "blue", "pink", "green", "orange", "yellow", "violet", "indigo")

SPEED = 10


class Car:

    def __init__(self):
        self.all_cars = []
        self.level_speed = 10

    def create_cars(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.goto(random.choice(POSITION))
        car.seth(180)
        self.all_cars.append(car)
        self.move_cars()

    def move_cars(self):
        for car in self.all_cars:
            car.forward(SPEED + self.level_speed)

    def next_level(self):
        self.level_speed += 10
        return self.level_speed

from turtle import Turtle

STARTING_POSITION = (0, -270)
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def move(self):
        self.forward(20)

    def reset_position(self):
        self.goto(STARTING_POSITION)

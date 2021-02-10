from turtle import Turtle

START_POSITION = (0, -230)
UP = 90
MOVE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.seth(UP)

    def up(self):
        self.forward(MOVE)

    def reset_position(self):
        self.goto(START_POSITION)

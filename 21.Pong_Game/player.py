from turtle import Turtle

UP = 90
MOVE = 20


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(UP)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            self.forward(MOVE)

    def down(self):
        if self.ycor() > -240:
            self.back(MOVE)

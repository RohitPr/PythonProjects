from turtle import Turtle

MOVE = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.X = 5
        self.Y = 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.X
        new_y = self.ycor() + self.Y
        self.goto(new_x, new_y)

    def bounce(self):
        self.Y *= -1

    def bat_collide(self):
        self.X *= -1

    def reset(self):
        self.showturtle()
        self.goto(0, 0)
        self.move()

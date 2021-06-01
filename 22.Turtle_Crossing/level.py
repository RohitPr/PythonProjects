from turtle import Turtle

FONT = ("Ariel", 20, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

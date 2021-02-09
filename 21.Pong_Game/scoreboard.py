from turtle import Turtle

FONT = ("Ariel", 30, "normal")


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score : {self.score2} - {self.score1}", align="center", font=FONT)

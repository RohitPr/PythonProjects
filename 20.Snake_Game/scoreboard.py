from turtle import Turtle

ALIGN = "center"
FONT = ("Ariel", 30, "italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score : {self.score}", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\n Your Final Score: {self.score}", move=False, align=ALIGN, font=FONT)

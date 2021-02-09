from turtle import Turtle

ALIGN = "center"
FONT = ("Ariel", 25, "normal")
END_FONT = ("Ariel", 35, "bold")

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-260, 260)
        self.color("black")
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def update_level(self):
        self.clear()
        self.level+= 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

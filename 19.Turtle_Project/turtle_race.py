from turtle import Turtle,Screen
import random

COLORS = ("red", "blue", "green", "yellow", "pink", "orange")
Y_POS = (-210, -140, -70, 0, 70, 140)
turtles_list = []

screen = Screen()
screen.screensize(canvwidth=600, canvheight=400)
user_choice = screen.textinput(title="Turtle Race", prompt="Choose the Color of the Turtle: ").lower()

for a in range(0, 6):
    tur = Turtle(shape="turtle")
    tur.penup()
    tur.turtlesize(2)
    tur.color(COLORS[a])
    tur.goto(-290, Y_POS[a])
    turtles_list.append(tur)

is_on = True

while is_on:
    turt = random.choice(turtles_list)
    turt.forward(random.randint(0, 10))
    if turt.xcor() > 290:
        is_on = False
        winner = turt.pencolor().title()

if user_choice == winner:
    print(f"You won. The winner is {winner} Turtle.")
else:
    print(f"You've lost. The winner is {winner} Turtle.")

screen.exitonclick()

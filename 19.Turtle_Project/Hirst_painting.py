import colorgram
import turtle
import random

pic = colorgram.extract("dot.jpg", 8)
colors = []

for a in pic:
    rgb_color = a.rgb
    red = rgb_color.r
    green = rgb_color.g
    blue = rgb_color.b
    final_color = (red, green, blue)
    colors.append(final_color)

tut = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

tut.hideturtle()
tut.penup()
y = -230
x = -260
A= 50
tut.goto(x, y)

for a in range(0, 10):
    for a in range(0, 10):
        tut.speed(0)
        tut.dot(size=25)
        tut.color(random.choice(colors))
        tut.penup()
        tut.forward(50),
        tut.pendown()
    tut.penup()
    tut.goto(x,y+A)
    A += 50

screen.bgcolor("white")
screen.screensize(canvwidth=600, canvheight=300)
screen.exitonclick()

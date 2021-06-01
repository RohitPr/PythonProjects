from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scorecard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = Player((450, 0))
player2 = Player((-450, 0))
ball = Ball()
score = Scorecard()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game = True
while game:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # Detect Bat Collision

    if player1.distance(ball) < 30 or player2.distance(ball) < 30:
        ball.bat_collide()

    # Detect Wall Collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect Ball Miss and Update Score

    if ball.xcor() > 510:
        time.sleep(0.5)
        ball.reset()
        score.score2 += 1
        score.update_scoreboard()

    if ball.xcor() < -510:
        time.sleep(0.5)
        ball.reset()
        score.score1 += 1
        score.update_scoreboard()

screen.exitonclick()

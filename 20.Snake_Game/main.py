from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food

    if snake.head.distance(food) < 15:
        food.new_position()
        snake.extend_snake()
        score.update_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        score.game_over()
        game = False

    # Detect Collision with Tail
    for parts in snake.snakes[1:]:
        if snake.head.distance(parts) < 10:
            score.game_over()
            game = False

screen.exitonclick()

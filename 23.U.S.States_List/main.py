import pandas
import turtle

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

states_guessed = []
score = 0
game = True

while game:
    user_input = screen.textinput(title="Guess the State", prompt="Guess: ").title()
    if user_input == "Exit":
        game = False
    if user_input in state_list:
        score += 1
        states_guessed.append(user_input)
        df = pandas.DataFrame(states_guessed)
        df.to_csv("States_Guessed.csv")
        screen.title(f"Your Score: {score}")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        x = int(state_data.x)
        y = int(state_data.y)
        t.goto(x, y)
        t.write(f"{user_input}", align="center", font=("Ariel,", 8, "normal"))



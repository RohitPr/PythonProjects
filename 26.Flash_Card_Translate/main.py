from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CHOSEN_WORD = ""
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(language_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_face, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(language_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_face, image=back_image)


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Translation Game")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_face = canvas.create_image(400, 265, image=front_image)
canvas.grid(row=0, column=0, columnspan=2, sticky="NSEW")

language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
language_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

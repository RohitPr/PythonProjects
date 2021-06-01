from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_text.config(text="Timer")
    canvas.itemconfig(countdown_text, text="00:00")
    tick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_text.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_text.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    timer_minute = math.floor(count / 60)
    timer_seconds = count % 60

    if timer_seconds < 10:
        timer_seconds = f"0{timer_seconds}"
    canvas.itemconfig(countdown_text, text=f"{timer_minute}:{timer_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        tick_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW)
timer_text.config(font=(FONT_NAME, 30, "bold"))
timer_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
countdown_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

tick_mark = Label(text="", fg=GREEN, bg=YELLOW)
tick_mark.grid(row=2, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

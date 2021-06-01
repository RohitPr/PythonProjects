import json
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += (random.choice(letters) for char in range(random.randint(8, 10)))
    password_list += (random.choice(symbols) for char in range(random.randint(2, 4)))
    password_list += (random.choice(numbers) for char in range(random.randint(2, 4)))

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(username) < 5 or len(password) < 8:
        messagebox.showwarning(title="Error Message", message="Username or Password too small")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Username: {username}\n"
                                                              f"Password: {password}")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=50)

canvas = Canvas(width=223, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(90, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1)

website_search = Button(text="Search", width=20, command=find_password)
website_search.grid(row=1, column=2)

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=40)
username_entry.insert(index=0, string="rohit@email.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="NSEW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

password_generate = Button(text="Generate Password", width=20, command=generate_password)
password_generate.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="NSEW")

window.mainloop()

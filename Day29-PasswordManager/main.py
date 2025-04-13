from tkinter import *
from tkinter import messagebox
import random
import string
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    symbols = list(string.punctuation)
    numbers = list(string.digits)
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    nr_letters = random.randint(8, 10)
    password_list = [random.choice(symbols + numbers + letters) for x in range(0, nr_letters + nr_numbers + nr_symbols)]
    new_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="File doesn't exist.")
    else:
        if website in data:
            if len(website):
                messagebox.showinfo(title=website, message="Username:" + data[website]["username"] +
                                                           "\nPassword:" + data[website]["password"])
            else:
                messagebox.showwarning(title="Warning", message="Please don't leave website field empty!")
        else:
            messagebox.showwarning(title="Warning", message=f"{website} doesn't exist.")
    finally:
        website_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    if len(website) and len(username) and len(password):
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
    else:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")


# ---------------------------- EXIT PROGRAM ------------------------------- #
def exit_program():
    window.quit()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=48)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generator_button = Button(text="Generate Password", width=14, command=generator)
generator_button.grid(column=2, row=3)
add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)
exit_button = Button(text="Exit", width=10, command=exit_program)
exit_button.grid(column=2, row=0)

window.mainloop()

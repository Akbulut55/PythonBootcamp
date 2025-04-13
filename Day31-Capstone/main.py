from tkinter import *
import pandas as pd
import random

word_data = pd.read_csv("data/1000-tr-ru.csv")
word_data_dict = word_data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    current_card = random.choice(word_data_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=current_card["ru"], fill="black")
    window.after(3000, func=flip_card)


def right_answer():
    word_data_dict.remove(current_card)
    next_card()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="Türkçe", fill="white")
    canvas.itemconfig(card_word, text=current_card["tr"], fill="white")


window = Tk()
window.title("Capstone Project")
window.config(padx=50, pady=50, background="#B1DDC6")
window.geometry("+300+30")

canvas = Canvas(width=800, height=526, highlightthickness=0, background="#B1DDC6")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="")
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()

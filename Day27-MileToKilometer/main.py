from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=110)

mile_entry = Entry(width=20, font=("Ariel", 12))
mile_entry.focus()
mile_entry.grid(column=1, row=0)

labels = ["Miles", "is equal to", "Km"]
for i, text in enumerate(labels):
    new_label = Label(text=text, font=("Ariel", 12))
    new_label.grid(column=0 if i == 1 else 2, row=i if i != 2 else 1)

calculated_label = Label(text=0, font=("Ariel", 12))
calculated_label.grid(column=1, row=1)


def calculate():
    calculated_label.config(text=round(int(mile_entry.get()) * 1.609))


calculate_button = Button(text="Calculate", font=("Ariel", 12), command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
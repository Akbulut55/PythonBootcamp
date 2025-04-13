from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=700, height=500)
window.config(padx=100, pady=100)

my_label = Label(text="I am a label", font=("ariel", 24))
my_label.config(padx=50, pady=50)
# my_label.place(x=300, y=250)
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=my_input.get())


button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=1, row=1)
button2 = Button(text="Dont click me")
button2.grid(column=2, row=0)

my_input = Entry(width=10)
my_input.insert(END, "hello")
my_input.focus()
my_input.grid(column=3, row=2)




window.mainloop()
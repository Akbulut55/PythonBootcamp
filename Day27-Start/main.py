from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=700, height=500)

# Label
my_label = Label(text="I am a label", font=("ariel", 24))
my_label.pack()

# Button
def button_clicked():
    my_label.config(text=my_input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
my_input = Entry(width=10)
my_input.insert(END, "hello")
my_input.focus()
my_input.pack()

# Text
my_text = Text(height=5, width=30)

my_text.insert(END, "Hello")
print(my_text.get("1.0", END))
my_text.pack()

# Spinbox
my_spinbox = Spinbox(from_=0, to=10, width=5)
my_spinbox.pack()

# Scale
my_scale = Scale(from_=0, to=100)
my_scale.pack(side="right")

# Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
my_checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
my_checkbox.pack()


# Radiobutton
def radiobutton_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=15, variable=radio_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option 2", value=30, variable=radio_state, command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox(height=4)
fruits = ["Banana", "Apple", "Pear", "Orange"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()






window.mainloop()
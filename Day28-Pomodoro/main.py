from tkinter import *
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
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", font=("Rockwell", 30, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break Time", font=("Rockwell", 30, "bold"), fg=PINK, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break Time", font=("Rockwell", 30, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work Time", font=("Rockwell", 30, "bold"), fg=RED, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global mark

    count_min = int(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        if reps % 2 == 0:
            for x in range(int(reps / 2)):
                mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Ariel", 24, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=("Rockwell", 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", width=8, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=8, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=10)
check_label.grid(column=1, row=3)

window.mainloop()

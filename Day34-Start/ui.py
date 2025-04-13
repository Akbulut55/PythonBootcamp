from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.label = Label(text="Score: 0", background=THEME_COLOR, highlightthickness=0,
                           padx=20, pady=20, foreground="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=250, height=300, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(125, 150, text="", width=220,
                                                     font=("Arial", 18, "italic"),
                                                     fill=THEME_COLOR)

        self.correct_img = PhotoImage(file="images/true.png")
        self.correct_btn = Button(image=self.correct_img, highlightthickness=0, command=self.correct)
        self.correct_btn.grid(column=0, row=2, padx=20, pady=20)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=self.wrong_img, highlightthickness=0, command=self.wrong)
        self.wrong_btn.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"Quiz is over.")
            self.label.config(text=f"Score: {self.quiz.score}")
            self.correct_btn.config(command="disabled")
            self.wrong_btn.config(command="disabled")
        else:
            (number, question) = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{number}:{question}")
            self.label.config(text=f"Score: {self.quiz.score}")

    def correct(self):
        answer = self.quiz.check_answer("True")
        if answer:
            self.quiz.score += 1
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")
        self.window.update()
        self.window.after(1000)
        self.canvas.config(background="White")
        self.get_next_question()

    def wrong(self):
        answer = self.quiz.check_answer("False")
        if answer:
            self.quiz.score += 1
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")
        self.window.update()
        self.window.after(1000)
        self.canvas.config(background="White")
        self.get_next_question()





from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def refresh_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        if self.l_score == 3 or self.r_score == 3:
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))

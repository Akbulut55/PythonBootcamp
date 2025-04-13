from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=-40, y=260)
        self.write(f"Score : {self.score}", font=("Ariel", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", font=("Ariel", 15, "normal"))

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=("Ariel", 20, "normal"))

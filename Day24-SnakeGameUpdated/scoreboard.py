from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=-100, y=260)
        self.write(f"Score : {self.score} High Score : {self.highscore}", font=("Ariel", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score} High Score : {self.highscore}", font=("Ariel", 15, "normal"))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}", font=("Ariel", 15, "normal"))

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=("Ariel", 20, "normal"))

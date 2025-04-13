from turtle import Turtle
import random


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(starting_position[0])

    def move(self):
        self.forward(20)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)


directions = [0, 180]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.starting_heading = 0
        self.starting_direction = 0
        self.move_speed = 0.06

    def move_up(self):
        self.forward(10)
        self.left(90)
        self.forward(20)
        self.right(90)

    def move_down(self):
        self.forward(8)
        self.right(90)
        self.forward(20)
        self.left(90)

    def set_direction(self):
        self.move_speed = 0.06
        self.goto(0, 0)
        self.starting_heading = random.randint(0, 1)
        self.starting_direction = random.randint(0, 1)
        self.setheading(directions[self.starting_heading])

    def change_direction(self, direction):
        self.setheading(directions[direction])
        self.move_speed *= 0.8

    def move(self):
        if self.starting_heading == 0:
            if self.starting_direction == 0:
                self.move_up()
            elif self.starting_direction == 1:
                self.move_down()
        elif self.starting_heading == 1:
            if self.starting_direction == 0:
                self.move_down()
            elif self.starting_direction == 1:
                self.move_up()

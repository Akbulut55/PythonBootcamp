from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.tutels = []
        self.create_snake()
        self.head = self.tutels[0]

    def create_snake(self):
        for positions in starting_positions:
            self.add_tutel(positions)

    def add_tutel(self, positions):
        new_tutel = Turtle(shape="square")
        new_tutel.color("lime")
        new_tutel.penup()
        new_tutel.goto(positions)
        self.tutels.append(new_tutel)

    def reset_snake(self):
        for x in range(0, len(self.tutels)):
            self.tutels[x].goto(1000, 1000)
        self.tutels.clear()
        self.create_snake()
        self.head = self.tutels[0]

    def extend(self):
        self.add_tutel(self.tutels[-1].position())

    def move(self):
        for tut_num in range(len(self.tutels) - 1, 0, -1):
            new_x = self.tutels[tut_num - 1].xcor()
            new_y = self.tutels[tut_num - 1].ycor()
            self.tutels[tut_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

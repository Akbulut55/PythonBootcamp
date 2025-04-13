import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.car_list = []

    def create_new_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-230, 250))
        self.car_list.append(new_car)

    def move_cars(self, car_num):
        self.car_list[car_num].forward(self.STARTING_MOVE_DISTANCE)



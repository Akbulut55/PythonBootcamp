from turtle import Turtle, Screen
import random

screen = Screen()
turtle_colors = ["red", "green", "blue", "orange", "purple"]
turtle_y_positions = [180, 90, 0, -90, -180]
turtles = []
is_race_on = False
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

for turtle_index in range(0, 5):
    new_tutel = Turtle(shape="turtle")
    new_tutel.color(turtle_colors[turtle_index])
    new_tutel.penup()
    new_tutel.goto(x=-320, y=turtle_y_positions[turtle_index])
    turtles.append(new_tutel)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == turtle.pencolor():
                print(f"You've won!The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost!The {winning_color} turtle is the winner.")
        random_movement = random.randint(0, 20)
        turtle.forward(random_movement)

screen.exitonclick()

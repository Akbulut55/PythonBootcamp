import turtle
import random

timmy_the_turtle = turtle.Turtle()

screen = turtle.Screen()
turtle.colormode(255)
# Draw a square
# for x in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# ------------------------------------------------------------------
# Draw gaps in straight line
# for x in range(0, 20):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
# ------------------------------------------------------------------
# Drawing regular polygons
# colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
# n = 2
# side = int(input("Side number?"))
# while not n == side:
#     n += 1
#     timmy_the_turtle.color(random.choice(colors))
#     for x in range(0, n):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(180 - (((n - 2) * 180) / n))
# ------------------------------------------------------------------
#
# #
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color = (r, g, b)
#     return rand_color
#
#
# timmy_the_turtle.speed(10)
# direction = [90, 180, 270, 360]
#
# for x in range(0, 50):
#     timmy_the_turtle.pensize(5)
#     timmy_the_turtle.shapesize(0.5, 0.5, 0.5)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.right(random.choice(direction))
#     timmy_the_turtle.forward(random.randint(20, 50))
# ------------------------------------------------------------------
# Draw spirograph


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


n = int(turtle.numinput("How many circles?", "Enter a number"))
timmy_the_turtle.speed(12)
for x in range(0, n):
    timmy_the_turtle.circle(100, 360)
    timmy_the_turtle.right(360 / n)
    timmy_the_turtle.color(random_color())
screen.exitonclick()

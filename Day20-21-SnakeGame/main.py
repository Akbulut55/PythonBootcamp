from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
apple = Food()
score_on_screen = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(apple) < 15:
        apple.refresh()
        score_on_screen.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score_on_screen.game_over()

    for tutel in snake.tutels[1:]:
        if snake.head.distance(tutel) < 10:
            game_is_on = False
            score_on_screen.game_over()

screen.exitonclick()

from turtle import Screen
from gameobjects import Paddle, Ball
from scoreboard import ScoreBoard
import time

starting_position1 = [(-500, 0)]
starting_position2 = [(500, 0)]

screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(starting_position1)
paddle2 = Paddle(starting_position2)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=paddle1.up, key="w")
screen.onkey(fun=paddle1.down, key="s")
screen.onkey(fun=paddle2.up, key="Up")
screen.onkey(fun=paddle2.down, key="Down")

game_is_on = True
match_is_on = True

while game_is_on:
    ball.set_direction()
    scoreboard.refresh_score()
    screen.update()
    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        break
    time.sleep(3)
    while match_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        if - 270 < paddle1.ycor() < 270:
            paddle1.move()
        if - 270 < paddle2.ycor() < 270:
            paddle2.move()
        ball.move()
        # bouncing from walls
        if ball.ycor() >= 320:
            if ball.starting_direction == 0:
                ball.starting_direction = 1
            elif ball.starting_direction == 1:
                ball.starting_direction = 0
        elif ball.ycor() <= -320:
            if ball.starting_direction == 0:
                ball.starting_direction = 1
            elif ball.starting_direction == 1:
                ball.starting_direction = 0
        # bouncing from paddles
        if paddle1.xcor() - 10 < ball.xcor() < paddle1.xcor() + 20 and paddle1.ycor() + 60 > ball.ycor() > paddle1.ycor() - 60:
            ball.change_direction(0)
        elif paddle2.xcor() + 10 > ball.xcor() > paddle2.xcor() - 20 and paddle2.ycor() + 60 > ball.ycor() > paddle2.ycor() - 60:
            ball.change_direction(1)
        # when paddle misses
        if ball.xcor() > 580:
            scoreboard.l_score += 1
            break
        elif ball.xcor() < -580:
            scoreboard.r_score += 1
            break
        if scoreboard.l_score == 3 or scoreboard.r_score == 3:
            break
screen.exitonclick()

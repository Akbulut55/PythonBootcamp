import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="w")

loop_count = 0
loop_number = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_count % loop_number == 0:
        cars.create_new_car()
    if player.ycor() == 280:
        player.restart()
        scoreboard.score += 1
        scoreboard.change_score()
        cars.STARTING_MOVE_DISTANCE += cars.MOVE_INCREMENT
        loop_number -= 1
    for x in range(0, len(cars.car_list)):
        cars.move_cars(x)
        if cars.car_list[x].distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    loop_count += 1
screen.exitonclick()

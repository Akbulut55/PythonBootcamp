from turtle import Turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("Cities of Türkiye")
background = "tr_harita.gif"
screen.addshape(background)
screen.setup(1415, 768)
screen.bgpic(background)
city_data = pandas.read_csv("locations.csv")
guessed_city_num = 0
life = 5
already_guessed = []
while guessed_city_num != 80:
    answer = screen.textinput(title=f"{guessed_city_num}/80 , Tries left: {life}", prompt="What's the next city?")
    all_cities = city_data.cities.to_list()
    if answer.title() in all_cities:
        if answer.title() not in already_guessed:
            already_guessed.append(answer.title())
            guessed_city_num += 1
            current_city = city_data[city_data.cities == answer.title()]
            new_tutel = Turtle()
            new_tutel.hideturtle()
            new_tutel.penup()
            new_tutel.goto(int(current_city.x), int(current_city.y))
            new_tutel.write(f"{current_city.cities.item()}", font=("Ariel", 14, "normal"))
    elif answer.lower() == "exit":
        missing_cities = [city for city in already_guessed if city not in all_cities]
        with open("missing_cities.txt", mode="w") as missing:
            missing.writelines(missing_cities)
        break
    else:
        if life == 0:
            new_tutel = Turtle()
            new_tutel.hideturtle()
            new_tutel.penup()
            new_tutel.goto(-170, 0)
            new_tutel.write("GAME OVER", font=("Ariel", 50, "normal"))
            break
        life -= 1
screen.exitonclick()

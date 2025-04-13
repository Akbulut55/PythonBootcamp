import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(200)
timmy.circle(100)
my_screen = turtle.Screen()
my_screen.exitonclick()

print(my_screen)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Charmander", "Squirtle", "Pikachu"])
table.add_column("Type", ["Fire", "Water", "Electric"])
table.align = "l"
print(table)

import turtle
from prettytable import PrettyTable



# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# my_screen = turtle.Screen()
# print(my_screen.canvwidth)
#
# timmy.color("coral")
# timmy.forward(100)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
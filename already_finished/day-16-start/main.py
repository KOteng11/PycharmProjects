# from turtle import Turtle, Screen
from prettytable import PrettyTable
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.penup()
# tim.forward(500)
#
# screen = Screen()
# screen.exitonclick()

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
])
print(table)

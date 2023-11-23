from turtle import Turtle
from turtle import Screen
import heroes

tim = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
#
# print(heroes.gen())

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# sides = 3
#
# while sides <= 10:
#     if sides == 3:
#         tim.color("cornflower blue")
#     elif sides == 4:
#         tim.color("dark slate gray")
#     elif sides == 5:
#         tim.color("saddle brown")
#     elif sides == 6:
#         tim.color("indian red")
#     elif sides == 7:
#         tim.color("dark orange")
#     elif sides == 8:
#         tim.color("indigo")
#     elif sides == 9:
#         tim.color("gold")
#     else:
#         tim.color("maroon")
#
#     for _ in range(sides):
#         angle = 360/sides
#         tim.forward(150)
#         tim.right(angle)
#     sides += 1
import random


colours = ["cornflower blue", "dark slate gray", "saddle brown", "indian red", "dark orange", "indigo", "gold", "maroon"]


def draw_shapes(sides):
    angle = 360/sides

    for _ in range(sides):
        tim.forward(150)
        tim.right(angle)


for num_of_sides in range(3, 11):
    tim.color(random.choice(colours))
    draw_shapes(num_of_sides)


screen = Screen()
screen.exitonclick()

import random
from turtle import Turtle
from turtle import Screen
import turtle


tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


def walk_randomly():
    angle = [0, 90, 180, 270]
    tim.forward(30)
    tim.setheading(random.choice(angle))


colours = ["cornflower blue", "dark slate gray", "saddle brown", "indian red", "dark orange", "indigo", "gold", "maroon"]

for _ in range(300):
    tim.speed("fastest")
    tim.pensize(10)
    tim.color(random_color())
    walk_randomly()

screen = Screen()
screen.exitonclick()


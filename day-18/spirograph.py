import random
import turtle as t


tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colour = (r, g, b)
    return random_colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(120)
        tim.right(size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()

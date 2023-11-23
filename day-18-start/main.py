from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
colors = ["cyan4", "blue", "chocolate", "DarkOrchid", "CadetBlue", "green", "DeepSkyBlue2", "coral3"]

def draw_shape(size):
    for _ in range(size):
        angle = 360 / size
        tim.forward(120)
        tim.right(angle)


count = 0
for sides in range(3, 11):
    tim.color(colors[count])
    draw_shape(sides)
    count += 1











screen = Screen()
screen.exitonclick()

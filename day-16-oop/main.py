# from turtle import Turtle, Screen
from prettytable import PrettyTable


def main():
    # tim = Turtle()
    # tim.shape("turtle")
    # tim.color("blue")
    # tim.forward(100)
    #
    # my_screen = Screen()
    # my_screen.exitonclick()

    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"
    print(table)

if __name__ == "__main__":
    main()

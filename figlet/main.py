import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = get_font(figlet)

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))


def get_font(f):
    list_of_fonts = []
    for font in f.getFonts():
        list_of_fonts.append(font)
    return list_of_fonts


if __name__ == "__main__":
    main()


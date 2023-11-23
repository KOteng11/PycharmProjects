import sys
from PIL import Image, ImageOps
import os


def main():
    if get_arguments() and check_extension():
        try:
            # Opens muppet image
            original_muppet = Image.open(sys.argv[1])
            # Opens shirt image
            shirt = Image.open("shirt.png")
            # get the size of the shirt
            size = shirt.size
            # crop the original picture to fit the size of the shirt
            muppet = ImageOps.fit(original_muppet, size)
            # paste the shirt on the muppet
            muppet.paste(shirt, shirt)
            # create an output
            muppet.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("File does not exist")


def check_extension():
    """
    This function checks if extensions for argument 1 and argument 2 ends with .jpg, .jpeg or png and
    exits the system if it doesn't. It also returns True if the extensions of both arguments matches
    else it exits the system
    :return: True
    """
    extensions = (".jpg", ".jpeg", ".png")
    if sys.argv[1].lower().endswith(extensions) and sys.argv[2].lower().endswith(extensions):
        argument_1 = os.path.splitext(sys.argv[1])
        argument_2 = os.path.splitext(sys.argv[2])

        if argument_1[1] == argument_2[1]:
            return True
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid Input")


def get_arguments():
    """
    Returns True if the number of command line arguments is equal to 3 and exists the system otherwise
    :return: True
    """
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True


if __name__ == "__main__":
    main()

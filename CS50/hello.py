import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        print("hello, my name is", sys.argv[1])


if __name__ == "__main__":
    main()



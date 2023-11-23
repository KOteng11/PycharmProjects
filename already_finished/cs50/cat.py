def main():

    while True:
        number = get_number()
        meow(number)


def get_number():
    while True:
        n = int(input("Enter number: "))
        if n >= 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()

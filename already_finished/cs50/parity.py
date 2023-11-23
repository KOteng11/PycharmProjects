def main():
    number = int(input("Number: "))

    if is_even(number):
        print("Even")
    else:
        print("Odd")


def is_even(num):
    return num % 2 == 0


main()

def main():
    fizz_buzz()


def fizz_buzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number = "FizzBuzz"
        elif number % 3 == 0:
            number = "Fizz"
        elif number % 5 == 0:
            number = "Buzz"

        print(number)


main()


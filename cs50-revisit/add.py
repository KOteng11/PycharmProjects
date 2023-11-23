import sys


def main():
    num1: float = get_int("Enter Number 1: ")
    num2: float = get_int("Enter Number 2: ")
    operation: list = ["add", "subtract", "multiply", "divide"]
    while True:
        choice: str = input("Choose operation: ").strip().lower()
        if choice in operation:
            break
    answer: float = 0
    match choice:
        case "add":
            answer = add(num1, num2)
        case "subtract":
            answer = subtract(num1, num2)
        case "multiply":
            answer = multiply(num1, num2)
        case _:
            answer = divide(num1, num2)
    print(f"{answer}")


def add(num1, num2) -> float:
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        sys.exit("Cannot divide by zero")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass



if __name__ == "__main__":
    main()
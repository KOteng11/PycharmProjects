def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    operator = input("Choose an operator (+, -, *, /, square): ")
    if operator == "+":
        total = add(x, y)
    elif operator == "-":
        total = subtract(x, y)
    elif operator == "*":
        total = multiply(x, y)
    elif operator == "/":
        total = divide(x, y)
    elif operator == "square":
        total = square(x)
    print(total)


def add(num1, num2):
    """
    Adds num1 and num 2 then return the total
    :param num1:
    :param num2:
    :return:
    """
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return round(num1 / num2, 2)


def square(num1):
    return num1 ** 2


main()

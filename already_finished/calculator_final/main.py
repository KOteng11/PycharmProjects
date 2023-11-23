# This program takes two numbers and depending on the operator which is '+', '-', '/', '*', add, subtract,
# divide, and multiply respectively

from art import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    number_1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new"
                              f"calculation: ").lower()
        if continue_calc == 'y':
            number_1 == answer

        else:
            should_continue = False
            calculator()


calculator()










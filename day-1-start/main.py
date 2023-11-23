def main():
    # Ask user for expression
    expression = input("Expression: ")
    # Split the expression by the space and assign to the variable x, y, z
    x, y, z = expression.split(" ")

    # Convert x and z to an integer
    x = int(x)
    z = int(z)

    # Check the operator and perform the necessary operation
    if y == "+":
        result = add(x, z)
    elif y == "-":
        result = subtract(x, z)
    elif y == "*":
        result = multiply(x, z)
    else:
        result = divide(x, z)

    # Display the results
    print(f"{result:.1f}")


def add(num1, num2):
    """
    This function adds num1 and num2 and then return the total
    :param num1:
    :param num2:
    :return: sum
    """
    return num1 + num2


def subtract(num1, num2):
    """
    This function subtracts num 2 from num1 and return the difference
    :param num1:
    :param num2:
    :return:
    """
    return num1 - num2


def multiply(num1, num2):
    """
    This function multiplies num1 and num2 and return the total
    :param num1:
    :param num2:
    :return:
    """
    return num1 * num2


def divide(num1, num2):
    """
    This function divides num2 from num1 and return the results
    :param num1:
    :param num2:
    :return:
    """
    return num1 / num2


main()

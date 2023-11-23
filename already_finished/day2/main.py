def add_numbers(numbers):
    """
    This function takes a string of numbers, converts to integer and adds them together
    :param numbers:
    :return:
    """
    global total

    for index in range(len(numbers)):
        total += int(numbers[index])

    return total


total = 0
str_digits = input("Type a two digit number: ")

print(add_numbers(str_digits))


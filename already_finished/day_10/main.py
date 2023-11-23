# def calculate(num1, num2):
#     total = num1 + num2
#
#     return total
#
#
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# result = calculate(num1=number1, num2=number2)
#
# print(result)

def format_name(fname, lname):
    """
    Take first and last name and format it to return the title case version of the name
    :param fname:
    :param lname:
    :return:
    """
    return f"{fname} {lname}".title()


firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")

full_name = format_name(firstname, lastname)
print(full_name)

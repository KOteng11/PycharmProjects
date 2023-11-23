# import random
#
#
# names = input("Enter names separated by comma: ").strip().title()
# names = names.split(", ")
# length = len(names)
# random_index = random.randint(0, length - 1)
# print(f"{names[random_index]} pays the bill today")


student_scores: list = input().split()
highest_score: int = 0
for each_score in student_scores:
    student_score = int(each_score)
    if student_score > highest_score:
        highest_score = student_score


print(f"The highest score is {highest_score}")

def myexpo(num1, num2) -> int:
    """

    :param num1: This is the base
    :param num2: This is the exponent
    :return: The result of the calculation
    """
    return num1 ** num2

print(myexpo)
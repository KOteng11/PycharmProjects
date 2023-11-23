"""
Instructions
You are going to write a program that calculates the highest score from a List of scores
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important
You are not allowed to use the max or min functions. The output words must match the example.
i.e.
The highest score in the class is: x
"""

student_scores = input("Input a list of student scores separated by a comma: ")
student_scores = student_scores.replace(" ", "")  # remove any spaces between the scores
student_scores = student_scores.split(",")  # convert the student_score to from a string to a list

highest_score = 0

for index in range(0, len(student_scores)):
    student_score = int(student_scores[index])  # convert student_score to an integer

    if student_score > highest_score:  # compare student_score to highest_score the find the larger score
        highest_score = student_score  # set highest_score to be the larger number

print(f"The highest score in the class is: {highest_score}")  # print the largest score

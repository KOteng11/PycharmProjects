"""
Instructions
You are going to write a program that calculaltes the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146

There are a total of 7 heights in student_heights
1146 / 7 = 163.714

Average height rounded to the nearest whole number = 164

important
You should not use the sum() or len() functions in your answer. You should try to replicate their functionality
using what you have learnt about for loops
"""

str_student_heights = input("Enter student heights separated by a comma: ")  # Ask user to enter student height
# separated by a comma

student_heights = str_student_heights.replace(" ", "")  # remove any spaces inbetween the student height
student_heights = student_heights.split(",")  # separate the student heights into a list

total = 0
count = 0

for index in range(0, len(student_heights)):
    student_heights[index] = int(student_heights[index])

    total += student_heights[index]  # the sum total of all the heights in the list
    count += 1  # number of students in the list
average = total / count
print(average)

#
# count = 0
# total = 0
#
# for student_height in student_heights:
#
#     int_student_height = int(student_height)
#     total += int_student_height
#
#     count += 1
#
# average = total / count
#
# print(f"Average height rounded to the nearest whole number is {average}")

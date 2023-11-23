"""
Instructions
You are going to write a program which will mark a spot with an X.
The map is made of 3 rows of blank squares.

Your program should allow you to enter the position of the treasure using a two-digit
system. The first digit is the horizontal column and the second digit is the vertical row number
"""

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map1 = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?: ")

horizontal = int(position[0])
vertical = int(position[1])

horizontal -= 1
vertical -= 1

map1[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")
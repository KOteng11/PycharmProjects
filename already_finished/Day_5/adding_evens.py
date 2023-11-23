"""
Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100

important
There should only be 1 print statement in your console output.
It should just print the final total and not every step of the calculation
"""

total = 0

for even_number in range(2, 101, 2):
    total += even_number

print(total)
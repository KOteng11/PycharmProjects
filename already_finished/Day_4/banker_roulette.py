"""
Instructions
You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important
You are not allowed to use the choice() function
"""
import random

names = input("Enter Everybody's name separated by a comma: ")

names = names.replace(" ", "")

individual_names = names.split(",")

num_of_items = len(individual_names)

choice = random.randint(0, num_of_items - 1)

print(f"{individual_names[choice]} is going to pay for the meal")

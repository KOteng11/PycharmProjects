import random


names_string = input("Give me everybody's names, separated by a comma. ")
names_string = names_string.replace(" ", "")
names = names_string.split(",")

index = random.randint(0, len(names)-1)
print(f"{names[index]} is going to pay for the meal")


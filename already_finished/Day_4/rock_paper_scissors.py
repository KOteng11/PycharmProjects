"""
Rules
Rock wins against scissors
Scissors wins against Paper
Paper wins against rock
"""
import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computerChoice = random.randint(0, 2)

game_image = [rock, paper, scissors]

if userChoice < 0 or userChoice > 2:
    print("You typed an invalid number, you lose")
elif userChoice == 0 and computerChoice == 2:
    print(f"{game_image[userChoice]}\nComputer chose:\n{game_image[computerChoice]}\nYou Win")
elif userChoice == 2 and computerChoice == 0:
    print(f"{game_image[userChoice]}\nComputer chose:\n{game_image[computerChoice]}\nYou Lose")
elif userChoice > computerChoice:
    print(f"{game_image[userChoice]}\nComputer chose:\n{game_image[computerChoice]}\nYou Win")
elif userChoice == computerChoice:
    print(f"{game_image[userChoice]}\nComputer chose:\n{game_image[computerChoice]}\nIt's a Draw")
else:
    print(f"{game_image[userChoice]}\nComputer chose:\n{game_image[computerChoice]}\nYou Lose")

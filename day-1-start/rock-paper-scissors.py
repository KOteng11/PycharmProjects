import random
from prettytable import PrettyTable

user_score = 0
computer_score = 0


def main():
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

    # Write your code below this line 👇
    user = get_hand("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: ")
    computer = random.randint(0, 2)

    images = [rock, paper, scissors]

    print(compare_choices(user, computer, images))


def score_board():
    global user_score
    global computer_score

    table = PrettyTable()
    table.align = "l"
    table.field_names = ["Score Board"]
    table.add_rows([
        {f"User Score: {user_score}"},
        {f"Computer Score: {computer_score}"}
    ])
    return table


def compare_choices(user_choice, computer_choice, game_image):
    global user_score
    global computer_score

    if user_choice == 0 and computer_choice == 2:
        return f"Player Score: {user_score}\nComputer Score: {computer_score}"
        user_score += 1
        return f"{game_image[user_choice]}\nComputer chose:\n{game_image[computer_choice]}\nYou Win"
    elif user_choice == 2 and computer_choice == 0:
        computer_score += 1
        return f"{game_image[user_choice]}\nComputer chose:\n{game_image[computer_choice]}\nYou Lose"
    elif user_choice > computer_choice:
        user_score += 1
        return f"{game_image[user_choice]}\nComputer chose:\n{game_image[computer_choice]}\nYou Win"
    elif user_choice == computer_choice:
        return f"{game_image[user_choice]}\nComputer chose:\n{game_image[computer_choice]}\nIt's a Draw"
    else:
        computer_score += 1
        return f"{game_image[user_choice]}\nComputer chose:\n{game_image[computer_choice]}\nYou Lose"


def get_hand(prompt):
    while True:
        try:
            user_hand = int(input(prompt))
            if user_hand < 0 or user_hand > 2:
                continue
            return user_hand
        except ValueError:
            pass


while True:
    play_game = input("Rock Paper Scissors. Type \"y\" to play or \"n\" to exit: ").lower()
    if play_game == "y":
        main()
    elif play_game == "n":
        print(f"\n{score_board()}")
        break
    else:
        continue

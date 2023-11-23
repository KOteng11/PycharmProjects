"""
You are going to write a virtual coin toss program. it will randomly tell the user "Heads" or Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads

"""
import random

# coinFlip = random.randint(0, 1)
#
# if coinFlip == 0:
#     print("Tails")
# else:
#     print("Heads")


def main():
    choice = input("Heads or Tails: ").lower()
    coin_toss_result = toss_coin(choice)
    print(check_results(coin_toss_result, choice))


def check_results(result, user_choice):
    if result == user_choice:
        return f"{result.capitalize()}, You win!"
    else:
        return f"{result.capitalize()}, You lose"


def toss_coin(toss):
    sides = ["heads", "tails"]
    return random.choice(sides)


main()

import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def get_random_number():
    return random.randint(1, 101)


def check_answer(random_num, guessed_num):
    if guessed_num > random_num:
        print("Too High")
    elif guessed_num < random_num:
        print("Too Low.")
    else:
        print(f"You got it! The answer was {random_num}")


def set_difficulty():
    level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_of_difficulty == 'easy':
        return EASY_LEVEL
    elif level_of_difficulty == 'hard':
        return HARD_LEVEL


def game():
    print(logo)
    random_number = get_random_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print(random_number)

    guess = 0
    turn = set_difficulty()

    while guess != random_number:
        print(f"You have {turn} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        check_answer(random_num=random_number, guessed_num=guess)

        turn -= 1
        if turn == 0:
            print(f"You lose. The answer was {random_number}")
            return


game()

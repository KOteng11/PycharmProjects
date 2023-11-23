import random
import sys


def main():
    level = get_int("Level: ")
    random_int = random.randint(1, level)
    while True:
        guess = get_int("Guess: ")

        guess_is_correct(random_int, guess)


def guess_is_correct(random_num, user_guess):
    if user_guess < random_num:
        print("Too small!")
    elif user_guess == random_num:
        print("Just right!")
        sys.exit()
    else:
        print("Too large!")


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                continue
            else:
                return number
        except ValueError:
            pass


if __name__ == "__main__":
    main()

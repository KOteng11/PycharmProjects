import random
import sys


def main():
    score = 0
    wrong_answer = 0

    # prompt user for level
    user_level = get_level("Level: ")
    print(user_level)

    # generate random numbers based on the level
    for _ in range(10):
        num_1 = generate_integer(user_level)
        num_2 = generate_integer(user_level)

        correct_answer = num_1 + num_2
        while wrong_answer < 3:
            try:
                user_answer = int(input(f"{num_1} + {num_2} = "))

                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    wrong_answer += 1
                    score -= 1
            except ValueError:
                print("EEE")
                wrong_answer += 1
                score -= 1

            if wrong_answer == 3:
                print(f"{num_1} + {num_2} = {correct_answer}")
                sys.exit()

    print(f"score: {score}")
    sys.exit()


def get_level(prompt):
    """
    accepts user input, check if input is between 1 and 3 inclusive and return user input
    """
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 3:
                return user_input
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)

    return number


if __name__ == "__main__":
    main()

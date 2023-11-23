import random


def main():
    # Initialize score and tries to 0
    score = 0

    user_level = get_level()

    # Ask 10 random questions
    for _ in range(5):
        tries = 0
        num_1 = generate_integer(user_level)
        num_2 = generate_integer(user_level)
        correct_answer = num_1 + num_2

        while tries < 3:
            try:
                user_answer = int(input(f"{num_1} + {num_2} = "))

                if is_correct(user_answer, correct_answer):
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{num_1} + {num_2} = {correct_answer}")

    print(f"score: {score}")


def is_correct(user_ans, correct_ans):
    return user_ans == correct_ans


def get_level():
    """
    accepts user input, check if input is between 1 and 3 inclusive and return user input
    """
    while True:
        try:
            user_input = int(input("Level: "))
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

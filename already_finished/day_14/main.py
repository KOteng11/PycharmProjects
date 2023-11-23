from art import logo, vs
import random
from game_data import data


def play_higher_lower():
    random_choice_b = random.choice(data)
    score = 0

    continue_playing = True
    print(logo)
    while continue_playing:
        random_choice_a = random_choice_b
        random_choice_b = random.choice(data)

        while random_choice_a == random_choice_b:
            random_choice_b = random.choice(data)

        print(f"{random_choice_a['name']}: {random_choice_a['follower_count']}")
        print(f"{random_choice_b['name']}: {random_choice_b['follower_count']}")

        print(f"Compare A: {random_choice_a['name']}, a {random_choice_a['description']}, from "
              f"{random_choice_a['country']}")
        print(vs)
        print(f"Against B: {random_choice_b['name']}, a {random_choice_b['description']}, from "
              f"{random_choice_b['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        num_of_followers_a = random_choice_a['follower_count']
        num_of_followers_b = random_choice_b['follower_count']

        if guess == 'a':
            if num_of_followers_a > num_of_followers_b:
                score += 1
                print(logo)
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                continue_playing = False
        elif guess == 'b':
            if num_of_followers_b > num_of_followers_a:
                score += 1
                print(logo)
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                continue_playing = False


play_higher_lower()

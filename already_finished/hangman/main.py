# Step 5

import random
import hangman_art
import hangman_words

end_of_game = False
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
print(chosen_word)

display = []
for _ in chosen_word:
    display.append("_")

print(display)

# while "".join(display) != chosen_word:     Alternative 1
# while "_" in display:     Alternative 2

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for index in range(0, word_length):
        letter = chosen_word[index]
        # print(f"Current position: {index}\n Current letter: {letter}\n Guessed letter: {guess}")
        if guess == letter:
            display[index] = letter
            # break

    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"the letter {guess} is not in the chosen word, you lose a life")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("you lose")
            break

    # print(f"{''.join(display)}")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    # has remaining
    print(hangman_art.stages[lives])

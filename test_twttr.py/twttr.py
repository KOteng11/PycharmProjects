def main():
    text = input("Text: ")
    print(shorten(text))

def shorten(word):
    new_word = ""
    for letter in word:
        match letter:
            case "a" | "e" | "i" | "O" | "u":
                letter = letter.replace(letter, "")
            case _:
                new_word += letter

    return new_word


if __name__ == "__main__":
    main()


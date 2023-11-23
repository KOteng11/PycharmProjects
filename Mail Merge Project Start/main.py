PLACEHOLDER = '[name]'
formatted_names = []
with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"./output/readytosend/letter_for_{stripped_name}", "w") as output_file:
            output_file.writelines(new_letter)

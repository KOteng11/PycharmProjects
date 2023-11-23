import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(txt, shift_number, cipher_direction):
    new_text = ""
    for char in txt:
        if char in alphabet:
            new_text += ""
            index = alphabet.index(char)
            if cipher_direction == "encode":
                index += shift_number
                new_text += alphabet[index]
            elif cipher_direction == "decode":
                index -= shift_number
                new_text += alphabet[index]
        else:
            new_text += char
    print(f"the {cipher_direction}d text is {new_text}")

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#  e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#  If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#  Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"Here's the {direction}d result: {end_text}")


end_program = False

while not end_program:
    text = input("Type your message:\n").lower()
    while True:
        shift = input("Type the shift number:\n")
        if shift.isnumeric():
            shift = int(shift)
            shift = shift % 26
            break
        else:
            print("Incorrect Choice.")
            continue

    # while True:
    #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #     if direction == 'encode':
    #         caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #         break
    #     elif direction == 'decode':
    #         caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #         break
    #     else:
    #         print("Incorrect option.\n")
    #         continue

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode':
            caesar(txt=text, shift_number=shift, cipher_direction=direction)

            break
        elif direction == 'decode':
            caesar(txt=text, shift_number=shift, cipher_direction=direction)
            break
        else:
            print("Incorrect option.\n")
            continue

    while True:
        run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.: ").lower()
        if run_again == "yes":
            break
        elif run_again == "no":
            end_program = True
            print("Goodbye")
            break
        else:
            print("Incorrect Input:")
            continue
    continue

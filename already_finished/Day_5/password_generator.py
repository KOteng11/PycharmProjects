import random

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_numbers = '0123456789'
ascii_symbols = '!#$%&()*+'

letters = list(ascii_letters)
numbers = list(ascii_numbers)
symbols = list(ascii_symbols)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password: "))
nr_symbols = int(input("How many symbols would you like in your password: "))
nr_numbers = int(input("How many numbers would you like in your password: "))
# password_length = int(input("What length of password do you require: "))
password = ""

# password += "".join(random.choices(letters, k=nr_letters))
# password += "".join(random.choices(symbols, k=nr_symbols))
# password += "".join(random.choices(numbers, k=nr_numbers))
#
# password = list(password)
# random.shuffle(password)
# password = "".join(password)
#
# print(password)

for random_letters in range(0, nr_letters):
    random_letters = random.choice(letters)
    password += random_letters

for random_symbols in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password += random_symbols

for random_numbers in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    password += random_numbers

password = list(password)
random.shuffle(password)
password = "".join(password)

print(password)






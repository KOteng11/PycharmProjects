"""
Write a program that adds the digits in a 2 digit number. e.g. if the
input was 35, then the output should be  3 + 5 = 8
"""

# variable to accept the digit
digits = input("Enter 2 digit number: ")

digit_1 = int(digits[0])  # Convert digit_1 to Integer

digit_2 = int(digits[1])  # Convert digit_2 to Integer

total = digit_1 + digit_2  # Add digit_1 + digit_2
print(f"{digit_1} + {digit_2} = {total}")  # Print the total

def check_number(num):
    return num % 2 == 0


number = int(input("Enter number: "))

if check_number(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")

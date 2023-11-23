print("Welcome to the tip calculator")  # display the welcome message

bill = float(input("What was the total bill?: "))  # accept the total bill as a string

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))  # accept the tip as a string

number_of_people = int(input("How many people to split the bill: "))

tip_amount = (tip/100)*bill

total_bill = bill + tip_amount

split_bill = "{:.2f}".format(total_bill/number_of_people)

print(f"Each person should pay: ${split_bill}")





def split_bill(bill_amount, tip, persons):
    tip_amount = (tip/100)*bill_amount
    total_bill = round(tip_amount + bill_amount, 2)
    individual_bill = total_bill / persons

    return "{:.2f}".format(individual_bill)


print("Welcome to the tip calculator")
bill = float(input("Enter the total bill: "))
tip_percent = int(input("Enter the percentage of tip you would like to give. 10, 12, or 15: "))
num_of_people = int(input("Enter the number of people splitting the bill: "))

bill = split_bill(bill, tip_percent, num_of_people)

print(f"Each person should pay: ${bill}")

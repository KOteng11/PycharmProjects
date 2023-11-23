"""
Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: +$1
"""

print("\nWelcome to Python Pizza Deliveries!")  # display banner
print("""
************************************************
    Small Pizza: $15
    Medium Pizza: $20
    Large Pizza: $25

    Pepperoni for Small Pizza: +$2
    Pepperoni for Medium or Large Pizza: +$3

    Extra cheese for any size pizza: +$1
***********************************************
""")

size = input("What size pizza do you want? S, M, or L: ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

if size == "s":
    bill += 15

elif size == "m":
    bill += 20

elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(bill)




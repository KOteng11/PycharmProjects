"""
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and
a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight(kg)/height**2 (m2)

It should tell them the interpretation of their BMI based on the BMI value.

    * Under 18.5 they are underweight
    * Over 18.5 but below 25 they have a normal weight
    * Over 25 but below 30 they are overweight
    * Over 30 but below 35 they are obese
    * Above 35 they are clinically obese
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/height**2)  # calculate BMI

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")

print(int(bmi))  # print BMI

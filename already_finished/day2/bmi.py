from prettytable import PrettyTable


def bmi_calculator():
    def message():
        print("\n\t\tWELCOME TO BMI CALCULATOR")
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Weight", "Interpretation"]
        table.add_row(["Under 18.5", "Underweight"])
        table.add_row(["Over 18.5 but below 25", "Normal Weight"])
        table.add_row(["Over 25 but below 30", "Overweight"])
        table.add_row(["Over 30 but below 35", "Obese"])
        table.add_row(["Above 35", "Clinically Obese"])
        return table

    def calculate_bmi(w, h):
        return int(w / h**2)

    def check_bmi(user_bmi):
        text = f"Your BMI is {user_bmi}"
        if user_bmi < 18.5:
            return text + ", You are underweight"
        elif user_bmi < 25:
            return text + ", You have a normal weight"
        elif user_bmi < 30:
            return text + ", You are overweight"
        elif user_bmi < 35:
            return text + ", You are obese"
        else:
            return text + ", You are clinically obese"

    print(message())
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))

    bmi = round(calculate_bmi(w=weight, h=height), 2)
    result = check_bmi(bmi)

    print(result)


continue_checking = True
while continue_checking:
    answer = input("\nType 'y' to check your BMI or 'n' to exit: ").lower()
    if answer == "y":
        bmi_calculator()
    else:
        continue_checking = False


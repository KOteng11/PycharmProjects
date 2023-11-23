import random
import sys


# SPLIT OR CHANCE


def main():
    print(logo())
    # Get bill from the waiter
    bill: float = get_bill()
    # Initialize tip to 0
    tip: float = 0

    while True:
        # Ask user if they want to give a tip
        tip_choice: str = (
            input('Enter "Yes" to give a tip or "No" to decline: ').lower().strip()
        )
        if tip_choice == "yes":
            while True:
                try:
                    # User want's to give a tip, ask for tip percentage
                    tip_percent: int = int(input("Enter tip percentage: %").strip())
                    break
                except ValueError:
                    pass
            # Calculate the tip amount
            tip_amount: float = calculate_tip(bill, tip_percent)
            tip += tip_amount
            break
        elif tip_choice == "no":
            break
        else:
            print("Invalid Input\n")

    # Calculate the total bill
    total_bill: float = calculate_total_bill(bill, tip)

    while True:
        try:
            user_choice: int = int(
                input('Enter "1" to SPLIT BILL or "2" to TREAT: ').strip()
            )
            if user_choice == 1:
                while True:
                    try:
                        number_of_people: int = int(input("Enter number of people: "))
                        break
                    except ValueError:
                        print("Invalid Input\n")
                # This calls the split function to split the bill
                bill_per_person: float = split_bill(total_bill, number_of_people)
                # Display the total bill in 2 decimal places
                print(f"\nTotal Bill: ${total_bill:.2f}")
                # Display bill per person
                print(f"Each person pays: ${bill_per_person:.2f}")
                sys.exit()
            elif user_choice == 2:
                while True:
                    # Accept each name separated by comma, remove white spaces from both ends and convert to lowercase
                    names: str = (
                        input("Enter names separated by comma: ").strip().title()
                    )
                    if "," in names:
                        break
                    else:
                        print("Invalid Input\n")
                # split names into a list
                names_lst: list = names.split(", ")
                random_person = random.choice(names_lst)
                print(f"\n{random_person} pays the total bill of ${total_bill:.2f}")
                print(f"Better luck next time {random_person}")
                sys.exit()
            else:
                raise ValueError()
        except ValueError:
            print("Invalid Input\n")


def split_bill(total_bill, number_of_people) -> float:
    """
    This function splits the total bill equally between the number of people
    :param total_bill: This is the total of the bill and tip
    :param number_of_people: The number of people the bill will be split between
    :return: The amount each person needs to pay
    """
    return round(total_bill / number_of_people, 2)


def calculate_total_bill(bill, tip) -> float:
    """
    This function returns the sum of bill and tip
    :param bill: bill received from the waiter
    :param tip: tip amount the user wants to give
    :return: the sum of the bill and tip in 2 decimal places
    """
    return round((bill + tip), 2)


def calculate_tip(bill_amount, tip_percent) -> float:
    """
    This function calculates and returns the tip amount
    :param bill_amount:
    :param tip_percent:
    :return:
    """
    return round((tip_percent / 100) * bill_amount, 2)


def get_bill() -> float:
    """
    This function asks user for bill and returns the bill
    :return:
    """
    while True:
        try:
            bill: float = float(input("Enter Bill: $").strip())
            return bill
        except ValueError:
            print("Invalid Amount\n")


def logo() -> str:
    return """
░▒█▀▀▀█░▄▀▀▄░█░░░▀░░▀█▀░░░▄▀▀▄░█▀▀▄░░░▀▀█▀▀░█▀▀▄░█▀▀░█▀▀▄░▀█▀
░░▀▀▀▄▄░█▄▄█░█░░░█▀░░█░░░░█░░█░█▄▄▀░░░░▒█░░░█▄▄▀░█▀▀░█▄▄█░░█░
░▒█▄▄▄█░█░░░░▀▀░▀▀▀░░▀░░░░░▀▀░░▀░▀▀░░░░▒█░░░▀░▀▀░▀▀▀░▀░░▀░░▀░

    """


if __name__ == "__main__":
    main()

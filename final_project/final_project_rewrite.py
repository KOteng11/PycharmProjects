import random
import re


def main():
    print(logo())
    # Get bill from the waiter
    bill = get_bill("Enter Bill: $")

    # Initialize tip to zero
    tip: float = 0

    while True:
        # Ask user if they want to give a tip
        tip_choice: str = (
            input('Enter "Yes" to give a tip or "No" to decline: ').lower().strip()
        )
        if tip_choice == "yes" or tip_choice == "no":
            break
        else:
            print("Invalid Choice\n")

    if tip_choice == "yes":
        while True:
            try:
                # User want's to give a tip, ask for tip percentage
                tip_percent: int = int(input("What percentage tip would you like to give? 10, 12, or 15? ").strip())
                if (
                    tip_percent == 10 or tip_percent == 12 or tip_percent == 15
                ):
                    break
                else:
                    print("Invalid Choice\n")
            except ValueError:
                print("Enter a number\n")
        # get the tip amount
        tip = get_tip(bill, tip_percent)

    # get the total amount (bill + tip)
    total_bill: float = calculate_total_bill(bill, tip)
    print(f"\nTotal Bill: {total_bill}")
    while True:
        try:
            # Ask the user to either split the bill or treat friends
            user_choice: int = int(
                input('Choose "1" to SPLIT or "2" to TREAT: ').strip()
            )
            if user_choice == 1 or user_choice == 2:
                break
            else:
                print("Invalid Choice\n")
        except ValueError:
            print("Invalid Choice\n")

    if user_choice == 1:
        while True:
            try:
                # Get the number of people to split the bill between
                number_of_people: int = int(
                    input("Enter number of people (Number should be more than 1): ")
                )
                if number_of_people > 1:
                    break
            except ValueError:
                print("Invalid number\n")
        # Split the bill between the number of people provided
        bill_per_person: float = split_bill(total_bill, number_of_people)
        print(f"Each person pays: ${bill_per_person:.2f}")
    else:
        while True:
            # Accept each name separated by comma, remove white spaces from both ends and convert to lowercase
            names: str = (
                input("Enter names separated by \",\": ").strip().title()
            )
            if re.search(
                r"^([a-zA-Z]+, ?[a-zA-Z]+)(, ?[a-zA-Z]+)*$", names, flags=re.IGNORECASE
            ):
                break
            else:
                print("Names must be separated by a \",\"")

        names_lst: list = names.split(",")
        random_person: str = random.choice(names_lst)
        print(
            f"\n{random_person.strip()} pays the total bill of ${total_bill:.2f} today."
        )


def split_bill(total_bill: float, number_of_people: int) -> float:
    """
    This function splits the total bill by the number of people and returns the bill per person
    :param total_bill: This is the total bill (bill + tip)
    :param number_of_people: This is the number of people to divide the total bill between
    :return: The bill per person
    """
    return round(total_bill / number_of_people, 2)


def calculate_total_bill(bill: float, tip: float) -> float:
    """
    This function sums the bill and the tip
    :param bill: The amount to be paid minus the tip
    :param tip: the tip amount
    :return: returns the total bill (bill + tip)
    """
    return round(bill + tip, 2)


def get_tip(bill: float, tip_percent: int) -> float:
    """
    This function calculates the tip to be given
    :param bill: The amount minus the tip
    :param tip_percent: The tip in percentage
    :return: the tip amount
    """
    return round((tip_percent / 100) * bill, 2)


def get_bill(prompt) -> float:
    while True:
        try:
            # Accept the bill
            bill: float = float(input(prompt).strip())
            if bill > 0:
                return bill
            else:
                print("Invalid Amount\n")
        except ValueError:
            print("Invalid Amount\n")


def logo() -> str:
    """
    :return: The logo
    """
    return """
░▒█▀▀▀█░▄▀▀▄░█░░░▀░░▀█▀░░░▄▀▀▄░█▀▀▄░░░▀▀█▀▀░█▀▀▄░█▀▀░█▀▀▄░▀█▀
░░▀▀▀▄▄░█▄▄█░█░░░█▀░░█░░░░█░░█░█▄▄▀░░░░▒█░░░█▄▄▀░█▀▀░█▄▄█░░█░
░▒█▄▄▄█░█░░░░▀▀░▀▀▀░░▀░░░░░▀▀░░▀░▀▀░░░░▒█░░░▀░▀▀░▀▀▀░▀░░▀░░▀░

    """


if __name__ == "__main__":
    main()

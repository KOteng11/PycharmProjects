import random
import re


class SplitOrTreat:
    @classmethod
    def get(cls):
        print("""
░▒█▀▀▀█░▄▀▀▄░█░░░▀░░▀█▀░░░▄▀▀▄░█▀▀▄░░░▀▀█▀▀░█▀▀▄░█▀▀░█▀▀▄░▀█▀
░░▀▀▀▄▄░█▄▄█░█░░░█▀░░█░░░░█░░█░█▄▄▀░░░░▒█░░░█▄▄▀░█▀▀░█▄▄█░░█░
░▒█▄▄▄█░█░░░░▀▀░▀▀▀░░▀░░░░░▀▀░░▀░▀▀░░░░▒█░░░▀░▀▀░▀▀▀░▀░░▀░░▀░
        """)

        while True:
            try:
                # Get bill from user
                bill: float = float(input("Enter bill: ").strip())
                if bill > 0:
                    return cls(bill)
                else:
                    print("Invalid Amount\n")
            except ValueError:
                print("Invalid Amount\n")

    def __init__(self, bill):
        self.bill = bill
        self.tip: int = 0

    @property
    def bill(self):
        return self._bill

    @bill.setter
    def bill(self, bill):
        self._bill = bill

    def get_tip(self):
        while True:
            try:
                # If user want's to give a tip, ask for the tip percentage
                tip_percent: int = int(input("What percentage tip would you like to give? 10, 12, or 15: ").strip())
                match tip_percent:
                    case 10 | 12 | 15:
                        break
                    case _:
                        print("Invalid Choice")
            except ValueError:
                print("Enter a number\n")
        self.tip += round((tip_percent / 100) * self.bill, 2)
        return self.tip

    def split_bill(self):
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
        bill_per_person: float = (self.bill + self.tip) / number_of_people
        return f"Each person pays: ${bill_per_person:.2f}"

    def treat(self):
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
        return f"\n{random_person.strip()} pays the total bill of ${self.bill + self.tip} today."


def main():
    tip = 0

    game = SplitOrTreat.get()

    while True:
        try:
            # Ask user if they want to give a tip
            tip_choice: str = input('Enter "Yes" to give a tip or "No" to decline: ').lower().strip()
            match tip_choice:
                case "yes" | "no":
                    break
                case _:
                    print("Invalid Choice\n")
        except ValueError:
            print("Invalid Choice\n")

    if tip_choice == "yes":
        tip = game.get_tip()

    total_bill = game.bill + tip

    print(f"\nTotal Bill: {total_bill}")
    while True:
        try:
            # Ask the user to either split the bill or treat friends
            user_choice: int = int(input('Choose "1" to SPLIT or "2" to TREAT: ').strip())
            if user_choice == 1 or user_choice == 2:
                break
            else:
                print("Invalid Choice\n")
        except ValueError:
            print("Invalid Choice")

    if user_choice == 1:
        print(game.split_bill())
    else:
        print(game.treat())


if __name__ == "__main__":
    main()

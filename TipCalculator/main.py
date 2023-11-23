def main():
    print("Welcome to the tip calculator.")
    bill: float = get_bill("What was the total bill? ")
    tip: float = get_tip("What percentage tip would you like to give? 10, 12, or 15? ", bill)
    total_bill: float = get_total_bill(bill, tip)
    number_of_people: int = get_number_of_people("How many people to split the bill? ")
    individual_bill: float = split_bill(total_bill, number_of_people)
    print(f"Each person should pay: ${individual_bill:.2f}")


def split_bill(total_bill, number_of_people) -> float:
    return round(total_bill / number_of_people, 2)


def get_number_of_people(prompt) -> int:
    while True:
        try:
            number_of_people = int(input(prompt))
            if number_of_people == 0:
                continue
            return number_of_people
        except ValueError:
            pass


def get_total_bill(bill, tip) -> float:
    return bill + tip


def get_bill(prompt) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass


def get_tip(prompt, bill) -> float:
    while True:
        try:
            percentage = [10, 12, 15]
            tip_percent = int(input(prompt))
            if tip_percent in percentage:
                return round(tip_percent/100 * bill, 2)
            continue
        except ValueError:
            pass


if __name__ == "__main__":
    main()

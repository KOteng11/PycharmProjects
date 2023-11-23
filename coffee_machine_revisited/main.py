import sys
from prettytable import PrettyTable

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def main():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if user_choice == "off":
            sys.exit("Goodbye")
        elif user_choice == "report":
            print(get_report())
        else:
            drink = get_drink(user_choice)

            if is_resource_sufficient(drink["ingredients"]):
                amount_payed = process_coins()
                cost_of_drink = drink["cost"]
                if is_transaction_successful(cost_of_drink, amount_payed):
                    print(make_coffee(drink["ingredients"], user_choice))
            else:
                sys.exit("Goodbye")


def make_coffee(ingredients, drink):
    for item in ingredients:
        resources[item] -= ingredients[item]

    return f"Here is your {drink}. Enjoy!"


def is_transaction_successful(cost, amount):
    global profit

    if amount == cost:
        profit += cost
        return True
    elif amount > cost:
        profit += cost
        change = amount - cost
        print(f"Here is ${change:.2f} as change.")
        return True
    else:
        print("Sorry that's not enough Money. Money refunded.")
        return False


def process_coins():
    total = 0
    while True:
        try:
            total += float(input("Insert Quarters: ")) * 0.25
            break
        except ValueError:
            pass

    while True:
        try:
            total += float(input("Insert Dimes: ")) * 0.10
            break
        except ValueError:
            pass

    while True:
        try:
            total += float(input("Insert Nickles: ")) * 0.05
            break
        except ValueError:
            pass

    while True:
        try:
            total += float(input("Insert Pennies: ")) * 0.01
            break
        except ValueError:
            pass

    return total


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def get_report():
    global profit

    print("**********************************")
    print("\t\t\tReport")
    table = PrettyTable()
    table.align = "l"
    table.add_column("Water", [f"{resources['water']}ml"])
    table.add_column("Milk", [f"{resources['milk']}ml"])
    table.add_column("Coffee", [f"{resources['coffee']}g"])
    table.add_column("Money", [f"${profit}"])
    return table


def get_drink(choice):
    while True:
        try:
            return MENU[choice]
        except KeyError:
            main()


if __name__ == "__main__":
    main()

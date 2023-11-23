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


def display_report():
    global money
    water = f'{resources["water"]}ml'
    milk = f'{resources["milk"]}g'
    coffee = f'{resources["coffee"]}g'

    table = PrettyTable()
    table.add_column("Water", [water])
    table.add_column("Milk", [milk])
    table.add_column("Coffee", [coffee])
    table.add_column("Profit", [f'${money}'])
    print(table)


def check_resource_sufficiency(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
        else:
            return True


def process_coins():
    quarters = float(input("Enter quarters: ")) * 0.25
    dimes = float(input("Enter dimes: ")) * 0.10
    nickles = float(input("Enter nickles: ")) * 0.05
    pennies = float(input("Enter pennies: ")) * 0.01

    total = round(quarters + dimes + nickles + pennies, 2)

    return total


def check_transaction(drink_cost, amount_paid):
    global money
    if drink_cost > amount_paid:
        print("Sorry that's not enough money. Money Refunded.")
        return False
    else:
        money += drink_cost
        change = "{:.2f}".format(amount_paid - drink_cost)
        print(f"Here is $ {change} in change")
        return True


def make_coffee(order_ingredients, choice):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {choice}. Enjoy!")


money = 0
is_on = True
while is_on:
    wrong_choice = True
    choice_options = ["espresso", "latte", "cappuccino", "off", "report"]
    while wrong_choice:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in choice_options:
            wrong_choice = False
    if user_choice == "off":
        order_coffee = False
    elif user_choice == "report":
        display_report()
    else:
        drink = MENU[user_choice]
        if check_resource_sufficiency(drink["ingredients"]):
            coins_inserted = process_coins()
            cost_of_drink = drink["cost"]
            if check_transaction(cost_of_drink, coins_inserted):
                make_coffee(drink["ingredients"], user_choice)

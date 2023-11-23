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
    global profit
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")


def is_resources_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    quarters = int(input("Enter quarters: ")) * 0.25
    dimes = int(input("Enter dimes: ")) * 0.10
    nickles = int(input("Enter nickles: ")) * 0.05
    pennies = int(input("Enter pennies: ")) * 0.01

    total = quarters + dimes + nickles + pennies

    return total


def is_transaction_successful(drink_cost, money_received):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here's your {drink_name}. Enjoy!")


is_on = True

profit = 0

while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        display_report()
    else:
        drink = MENU[choice]
        if is_resources_available(drink['ingredients']):
            cost_of_drink = drink['cost']
            amount_payed = process_coins()
            if is_transaction_successful(cost_of_drink, amount_payed):
                make_coffee(choice, drink['ingredients'])



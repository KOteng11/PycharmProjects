from coffee_data import MENU, resources, menu_display

QUARTERS = 0.25
DIME = 0.10
PENNY = 0.01
NICKEL = 0.05


def format_report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def resource_available(drink, menu):
    """
    This function checks if compares resources available to the resources needed and returns True if there are
    resources available and False if there are no resources available
    :param drink:
    :param menu:
    :return:
    """
    available_water = resources["water"]
    available_milk = resources["milk"]
    available_coffee = resources["coffee"]
    water_needed = 0
    milk_needed = 0
    coffee_needed = 0

    if drink in menu:
        items = menu[drink]
        water_needed = items['ingredients']['water']
        if drink == 'espresso':
            milk_needed = 0
        else:
            milk_needed = items['ingredients']['milk']
        coffee_needed = items['ingredients']['coffee']

    if available_water > water_needed:
        if available_milk > milk_needed:
            if available_coffee > coffee_needed:
                return True
            else:
                print("Sorry, there isn't enough Coffee")
                return False
        else:
            print("Sorry, there isn't enough Milk")
            return False
    else:
        print("Sorry, there isn't enough Water")
        return False


def set_cost(drink, menu):
    """
    This method finds the drink in the menu and return the cost of that drink
    :param drink:
    :param menu:
    :return: cost
    """
    if drink in menu:
        return menu[drink]['cost']


def process_coins(drink_cost):
    """
    This function accepts money from users and return the total amount
    :param drink_cost:
    :return: total_amount
    """
    num_of_quarters = 0
    num_of_dimes = 0
    num_of_nickles = 0
    num_of_pennies = 0
    print(f"This will cost ${drink_cost}. Please insert coins.")
    is_quarters = True
    while is_quarters:
        try:
            num_of_quarters = int(input("How many quarters?: "))
            is_quarters = False
        except ValueError:
            print("Incorrect Input.")

    is_dime = True
    while is_dime:
        try:
            num_of_dimes = int(input("How many dimes?: "))
            is_dime = False
        except ValueError:
            print("Incorrect Input.")

    is_nickles = True
    while is_nickles:
        try:
            num_of_nickles = int(input("How many nickles?: "))
            is_nickles = False
        except ValueError:
            print("Incorrect Input.")

    is_pennies = True
    while is_pennies:
        try:
            num_of_pennies = int(input("How many pennies?: "))
            is_pennies = False
        except ValueError:
            print("Incorrect Input")

    total_amount = ((num_of_quarters * QUARTERS) + (num_of_dimes * DIME) + (num_of_nickles * NICKEL) +
                    (num_of_pennies * PENNY))

    return total_amount


def check_transaction(cost, amount, drink):
    water_needed = 0
    milk_needed = 0
    coffee_needed = 0
    if drink in MENU:
        items = MENU[drink]
        water_needed = items['ingredients']['water']
        if drink == 'espresso':
            milk_needed = 0
        else:
            milk_needed = items['ingredients']['milk']
        coffee_needed = items['ingredients']['coffee']

    if amount < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif amount > cost:
        change = amount - cost
        resources['money'] += cost
        resources['water'] -= water_needed
        resources['milk'] -= milk_needed
        resources['coffee'] -= coffee_needed
        print(f"Here is ${round(change, 2)} in change.")
        print("Here is your expresso ☕. Enjoy!")
    else:
        resources['money'] += cost
        resources['water'] -= water_needed
        resources['milk'] -= milk_needed
        resources['coffee'] -= coffee_needed
        print("Here is your expresso ☕. Enjoy!")


def order_coffee():
    is_on = True

    print(menu_display)
    while is_on:

        # cost_of_drink = 0
        # amount_payed = 0

        user_choice = input("\tWhat would you like? (espresso/latte/cappuccino): ").lower()
        cost_of_drink = set_cost(user_choice, MENU)

        if user_choice == 'espresso':
            is_resource_available = resource_available(user_choice, MENU)
            if is_resource_available:
                amount_payed = process_coins(cost_of_drink)
                check_transaction(cost_of_drink, amount_payed, user_choice)
            else:
                is_on = False
        elif user_choice == 'latte':
            is_resource_available = resource_available(user_choice, MENU)
            if is_resource_available:
                amount_payed = process_coins(cost_of_drink)
                check_transaction(cost_of_drink, amount_payed, user_choice)
            else:
                is_on = False
        elif user_choice == 'cappuccino':
            is_resource_available = resource_available(user_choice, MENU)
            if is_resource_available:
                amount_payed = process_coins(cost_of_drink)
                check_transaction(cost_of_drink, amount_payed, user_choice)
            else:
                is_on = False
        elif user_choice == 'off':
            is_on = False
        elif user_choice == "report":
            format_report()
        else:
            print("Incorrect Choice")


order_coffee()


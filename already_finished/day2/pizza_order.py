from prettytable import PrettyTable


def order_pizza():
    def message():
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Welcome to Python Pizza Deliveries!"]
        table.add_rows([
            ["Small Pizza: $15"],
            ["Medium Pizza: $20"],
            ["Large Pizza: $25"],
            ["Pepperoni for Small Pizza: +$2"],
            ["pepperoni for Medium or Large Pizza: +$3"],
            ["Extra cheese for any size Pizza: +$1"]

        ])
        return table

    def check_pizza(pizza_size, pepperoni, more_cheese):
        amount = 0
        if pizza_size == "s":
            amount += 15
        elif size == "m":
            amount += 20
        else:
            amount += 25

        if more_cheese == "y":
            amount += 1
        if pepperoni == "y":
            if pizza_size == "s":
                amount += 2
            else:
                amount += 3
        return amount

    continue_ordering = True

    while continue_ordering:
        print(message())
        choice = input("Type 'Y' to order pizza or 'N' to quit: ").lower()
        if choice == 'y':
            size = input("What size pizza do you want? S, M, or L: ").lower()
            add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
            extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

            bill = check_pizza(size, add_pepperoni, extra_cheese)

            print(f"Your final bill is: ${bill}")
        else:
            continue_ordering = False


order_pizza()

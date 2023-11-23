def main():
    pizza_deliveries()


def pizza_deliveries():
    order_pizza = True

    while order_pizza:
        print("Thank you for choosing Python Pizza Deliveries!")
        print("""
        **********************************************
        Small Pizza (S): $15
        Medium pizza (M): $20
        Large pizza (L): $25
        Add pepperoni for small pizza: +$2
        Add pepperoni for medium or large pizza: +$3
        Add extra cheese for any size pizza: +$1
        **********************************************
        """)
        bill: int = 0
        while True:
            size: str = input("What size pizza do you want? S, M, or L: ").strip().lower()
            if size == "s" or size == "m" or size == "l":
                break
        while True:
            add_pepperoni: str = input("Do you want pepperoni? Y or N: ").strip().lower()
            if add_pepperoni == "y" or add_pepperoni == "n":
                break
        while True:
            extra_cheese: str = input("Do you want extra cheese? Y or N: ").strip().lower()
            if extra_cheese == "y" or extra_cheese == "n":
                break

        if size == "s":
            bill += 15
        elif size == "l":
            bill += 20
        else:
            bill += 25
        if add_pepperoni == "y":
            if size == "s":
                bill += 2
            else:
                bill += 3
        if extra_cheese == "y":
            bill += 1

        print(f"Your final bill is: ${bill}\n")
        while True:
            continue_ordering = input("Do you want to order another pizza? Y or N: ").strip().lower()
            if continue_ordering == "y" or continue_ordering == "n":
                break
        if continue_ordering == "y":
            pizza_deliveries()
        else:
            order_pizza = False



if __name__ == "__main__":
    main()



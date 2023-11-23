from prettytable import PrettyTable
from message import table_1


class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


class User(Person):
    def __init__(self, name, address, phone_number, user_size, pepperoni, more_cheese):
        super().__init__(name, address, phone_number)
        self.size = user_size
        self.add_pepperoni = pepperoni
        self.extra_cheese = more_cheese
        self.bill = 0

    def place_order(self):
        if self.size == 's':
            self.bill += 15
        elif self.size == 'm':
            self.bill += 20
        else:
            self.bill += 25

        if self.add_pepperoni == 'y':
            if self.size == 's':
                self.bill += 2
            else:
                self.bill += 3

        if self.extra_cheese == 'y':
            self.bill += 1

        return self.bill

    def print_receipt(self):
        table_2 = PrettyTable()
        table_2.align = "l"
        table_2.field_names = ["Receipt"]
        table_2.add_rows([
            [f"Name: {self.name}"],
            [f"Address: {self.address}"],
            [f"Phone: {self.phone_number}"],
            [f"Total Bill: {self.bill}"]
        ])
        print("\nHere is your Receipt")
        print(table_2)


continue_ordering = True
while continue_ordering:
    user_choice = input("Do you want to place an order? 'y' or 'n': ").lower()
    if user_choice == 'y':
        print(table_1)  # table_1 is imported from a module
        size = input("What size of pizza do you want. S, M, or L: ").lower()
        add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
        extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
        user_name = input("Enter your name: ").title()
        user_address = input("Enter your address: ").title()
        user_phone = input("Enter your phone number: ")

        user_1 = User(name=user_name, address=user_address, phone_number=user_phone, user_size=size,
                      pepperoni=add_pepperoni, more_cheese=extra_cheese)
        user_1.place_order()
        user_1.print_receipt()
    else:
        continue_ordering = False

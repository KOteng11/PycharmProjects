from modules.person import Person


class Waiter(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname, age)

    def take_order(self):
        ...

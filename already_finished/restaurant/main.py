class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Chef(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def cook(self):
        pass

class Waiter(Person):
    def __init__(self, firstname, lastname):

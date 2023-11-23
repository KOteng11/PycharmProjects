class Person:
    @classmethod
    def get_employee(cls):
        while True:
            try:
                firstname = input("Enter firstname: ")
                if not firstname:
                    raise ValueError("Missing firstname")
                elif not firstname.isalpha():
                    raise ValueError("Firstname cannot be a numbers")
                else:
                    break
            except ValueError:
                pass

        while True:
            try:
                lastname = input("Enter lastname: ")
                if not lastname:
                    raise ValueError("Missing lastname")
                elif not lastname.isalpha():
                    raise ValueError("Lastname cannot be a number")
                else:
                    break
            except ValueError:
                pass

        while True:
            try:
                age = int(input("Enter age: "))
                if not age:
                    raise ValueError("Missing age")
                else:
                    break
            except ValueError:
                pass

        return cls(firstname, lastname, age)

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old"



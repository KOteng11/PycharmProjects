class Guest:
    @classmethod
    def get_guest(cls):
        while True:
            try:
                firstname = input("Enter firstname: ")
                if not firstname:
                    raise ValueError("Missing firstname")
                elif not firstname.isalpha():
                    raise ValueError("Firstname must be alphabets")
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
                    raise ValueError("Lastname must be alphabets")
                else:
                    break
            except ValueError:
                pass

        while True:
            try:
                phone = int(input("Enter phone number: "))
                if not phone:
                    raise ValueError("Missing phone number")
                break
            except ValueError:
                pass

        while True:
            try:
                email = input("Enter email: ")
                if not email:
                    raise ValueError("Missing email")
                break
            except ValueError:
                pass

        return cls(firstname, lastname, phone, email)

    def __init__(self, firstname, lastname, phone, address):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def make_order(self):
        ...


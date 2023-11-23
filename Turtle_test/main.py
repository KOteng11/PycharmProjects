class Employee:
    def __init__(self, fname, lname, age, email, phone):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.phone = phone

    def age_in_10_yrs(self):
        return self.age + 10


class Manager(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.fname = "Kingsley"
        self.lname = "Oteng"
        self.age = 32
        self.email = "Kingsley_Oteng@outlook.com"
        self.phone = "4126540928"


manager1 = Manager()
print(manager1.fname)


class Person:
    amount = 0

    @classmethod
    def get_input(cls):
        while True:
            name = input("Enter name: ")
            if name:
                break
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                continue
        while True:
            try:
                height = int(input("Enter height: "))
                break
            except ValueError:
                continue
        return cls(name, age, height)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def __del__(self):
        Person.amount -= 1


class Worker(Person):
    @classmethod
    def get_input(cls):
        while True:
            name = input("Enter name: ")
            if name:
                break
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                continue
        while True:
            try:
                height = int(input("Enter height: "))
                break
            except ValueError:
                continue
        salary = float(input("Enter Salary: "))
        return cls(name, age, height, salary)

    def __init__(self, name, age, height, salary):
        super().__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12

    def __add__(self, other):
        return self.salary + other.salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}, Salary: {self.salary}"


def main():
    worker_1 = Worker.get_input()
    worker_2 = Worker.get_input()
    print(worker_1)
    print(worker_1.calc_yearly_salary())
    print(worker_1 + worker_2)


if __name__ == "__main__":
    main()




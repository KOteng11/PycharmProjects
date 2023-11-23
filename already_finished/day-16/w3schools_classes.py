# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#
#
# p1 = Person("John", 36)
#
# p1.myfunc()
#
# p1.age = 40
#
# print(p1.age)

# INHERITANCE - allows us to define a class that inherits all the methods and properties from another class
#  PARENT CLASS - is the class being inherited from, also called base class
#  CHILD CLASS - is the class that inherits from another class, also called derived class
# POLYMORPHISM - is often used in Class methods, where we can have multiple classes with the same method name.
#  E.g. say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def move(self):
        print("Drive!")


class Boat(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


# class Person:
#     def __init__(self, fname, lname, age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#
#     def printdetails(self):
#         print(self.fname, self.lname, self.age)
#
# # x = Person("Kingsley", "Darko", 34)
# # x.printdetails()
#
#
# # class Student(Person):
# #     def __init__(self, fname, lname, age):
# #         Person.__init__(self, fname, lname, age)
# #
# #
# # x = Student("Kingsley", "Darko", 34)
# # x.printdetails()
#
# class Student(Person):
#     def __init__(self, fname, lname, age, year):
#         super().__init__(fname, lname, age)
#
#         self.graduationyear = year
#
#
# x = Student("Kingsley", "Oteng", 24, 2019)
# print(x.graduationyear)
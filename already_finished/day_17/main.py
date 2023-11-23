class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class User(Person):
    def __init__(self, user_id, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age)
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Kingsley", "Darko", 34, "Klinston")
user_2 = User("002", "Oteng", "Koffie", 29, "Kay")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


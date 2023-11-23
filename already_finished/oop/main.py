# class User:
#     active_users = 0
#
#     def __init__(self, fname, lname, email):
#         self.firstname = fname
#         self.lastname = lname
#         self.email = email
#         User.active_users += 1
#
#     def full_name(self):
#         return f"{self.firstname} {self.lastname}"
#
#     def initials(self):
#         return f"{self.firstname[0]}.{self.lastname[0]}"
#
#     def logout(self):
#         User.active_users -= 1
#         return f"{self.firstname} has logged out"
#
#
# user_1 = User("Kingsley", "Darko", "klinston69@gmail.com")
# user_2 = User("Kingsley", "Darko", "klinston69@gmail.com")
# user_3 = User("Kingsley", "Darko", "klinston69@gmail.com")
#
# print(User.active_users)
# print(user_2.logout())
# print(User.active_users)




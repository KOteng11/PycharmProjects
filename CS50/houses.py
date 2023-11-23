# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
#
#
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
#
#
# gryffindors = filter(is_gryffindor, students)
#
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])


students = ["hermione", "Harry", "Ron"]
#
# gryffindors = {student: "Gryffindor" for student in students}
#
# print(gryffindors)

for i, student in enumerate(students):
    print(i + 1, student)
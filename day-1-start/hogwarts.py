from prettytable import PrettyTable

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

table = PrettyTable()
table.align = "l"
table.field_names = ["Name", "House", "Patronus"]
for student in students:
    table.add_row([student["name"], student["house"], student["patronus"]])
print(table)

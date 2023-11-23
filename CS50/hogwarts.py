# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]
#
# for student in students:
#     if student["name"] == "Hermione":
#         print(student["name"], student["house"], student["patronus"], sep=", ")
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * 3)


if __name__ == "__main__":
    main()
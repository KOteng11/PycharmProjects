import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        favorite = row["name"]
        print(favorite)
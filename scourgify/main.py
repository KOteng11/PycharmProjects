import csv
import sys


def main():
    if check_arguments():
        if check_csv():
            students = format_old_file()
            create_new_file(students)
        else:
            sys.exit("Not a CSV file")


def create_new_file(lst_students):
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow({"firstname": "firstname", "lastname": "lastname", "house": "house"})
        writer = csv.DictWriter(file, fieldnames=["firstname", "lastname", "house"])
        writer.writerows(lst_students)


def format_old_file():
    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lastname, firstname = row["name"].split(",")
                lastname = str(lastname).strip()
                firstname = str(firstname).strip()
                house = str(row["house"]).strip()
                students.append({"firstname": firstname, "lastname": lastname, "house": house})
            return students
    except FileNotFoundError:
        sys.exit("File does not Exist")


def check_csv():
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        return True
    else:
        return False


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True


if __name__ == "__main__":
    main()

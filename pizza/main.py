import sys
from tabulate import tabulate
import csv


def main():
    table = []
    if len(sys.argv) < 2:

        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)

                    for row in reader:
                        table.append(row)
                    print(tabulate(table, headers=table[0], tablefmt="grid"))
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()

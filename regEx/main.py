import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d\d?|1\d?\d?|2[0-4]?\d?|2[0-5]?[0-5]?)\.(\d\d?|1\d?\d?|2[0-4]?\d?|2[0-5]?[0-5]?)\."
                        r"(\d\d?|1\d?\d?|2[0-4]?\d?|2[0-5]?[0-5]?)\.(\d\d?|1\d?\d?|2[0-4]?\d?|2[0-5]?[0-5]?)$", ip)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

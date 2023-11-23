import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    txt = re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(txt)


if __name__ == "__main__":
    main()

import logging

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        try:
            number = int(input("What's n: "))
            if number > 0:
                return number
        except ValueError:
            pass
        except Exception as e:
            print(logging.exception(e))


def meow(n):
    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()
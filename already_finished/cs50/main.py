def main():
    # Ask user for their name, remove whitespace and capitalize
    name = input("What's your name: ").strip().title()

    print(hello(name))


def hello(username):
    return f"Hello, {username}"


main()

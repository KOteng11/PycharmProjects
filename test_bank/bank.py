def main():
    greet = input("Greeting: ").strip().lower()

    print(value(greet))


def value(greeting):
    amount = 100

    if greeting[0:5] == "hello":
        return f"${amount}"
        return amount
    elif greeting[0] == "h" and greeting[0:5] != "hello":
        amount += 20
        return f"${amount}"
    else:
        amount += 0
        return f"${amount}"


if __name__ == "__main__":
    main()

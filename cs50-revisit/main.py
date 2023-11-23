def main():
    print(message())
    while True:
        city = input("What's name of the city you grew up in: ")
        if city:
            break

    while True:
        pet = input("What's your pet's name: ")
        if pet:
            break

    print(f"your band name could be {city} {pet}")


def message():
    return "Welcome to the Band Name Generator."



if __name__ == "__main__":
    main()

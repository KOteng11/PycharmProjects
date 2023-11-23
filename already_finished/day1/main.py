def generate_band_name(city, pet):
    """

    :param city:
    :param pet:
    :return: a combined string of city and pet
    """
    return f"{city}{pet}"


print("Welcome to Band Name Generator.")
city = input("Enter the name of the city you grew up in: ")
pet = input("Enter the name of your pet: ")
band_name = generate_band_name(city, pet)

print(band_name)
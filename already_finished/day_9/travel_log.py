"""
Instructions
You are going to write a program that adds to a travel_log. You see a travel_log which is a List that contains 2
Dictionaries.

Write a function that will work with the following line of code on line 21. to add the entry for Russia to the
travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

HINT
1. Look at the function call above to see what the name of the function should be.
2. The inputs for the function are positional arguments. The order is very important.
3. Feel free to choose your own parameter names
"""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above
# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests


def add_new_country(country_visited, number_of_times_visited, cities_visited):
    new_country = {"country": country_visited, "visits": number_of_times_visited, "cities": cities_visited}

    travel_log.append(new_country)


# 🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

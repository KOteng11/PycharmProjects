MAX_AGE = 90


def display_life_in_weeks(user_age):
    remaining_years = MAX_AGE - user_age

    remaining_days = 365 * remaining_years
    remaining_weeks = 52 * remaining_years
    remaining_months = 12 * remaining_years

    return f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."


age = int(input("Enter your current age: "))

print(display_life_in_weeks(age))

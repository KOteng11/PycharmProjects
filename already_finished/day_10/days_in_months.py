"""
INSTRUCTIONS
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function
is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and
return False if it is not a leap year

You are then going to create a function called days_in_month() which will take a year and a month as input, e.g.

days_in_month(year=2022, month=2)

and it will use this information to work out the number of days in the month, then return that as the output, e.g.

28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year
has 29 days in February
"""


def is_leap(yyyy):
    if yyyy % 4 == 0:
        if yyyy % 100 == 0:
            if yyyy % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(yyyy, mm):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    number_of_days = month_days[mm - 1]

    if is_leap(yyyy) and mm == 2:
        return number_of_days + 1
    return number_of_days

# 🚨 Do NOT change any of the code below


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))


days = days_in_month(year, month)
print(days)

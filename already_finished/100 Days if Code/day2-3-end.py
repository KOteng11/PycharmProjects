"""
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90
years old.

It will take your current age as the input and output a message with our time left in this format:

    You have x days, y weeks, and z months left

Where x, y and z are replaced with the actual calculated numbers.

Warning: your output should match the words in the example output precisely. You should round the results to the nearest
whole number.
"""
MAX_AGE = 90

age = input("What is your current age?: ")  # Accept age as a string and store it in the age variable

int_age = int(age)  # Convert age from string to Integer

age_left = MAX_AGE - int_age

age_in_days = 365 * age_left  # Calculate age in days and store it in age_in_days variable
age_in_weeks = 52 * age_left  # Calculate age in weeks and store it in age_in_weeks variable
age_in_months = 12 * age_left  # Calculate age in months and store it in age_in_months variable

print(f"You have {age_in_days}, {age_in_weeks}, and {age_in_months} left")

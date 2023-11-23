from datetime import date
import sys
import operator
import re
import inflect


def main():
    dob = get_date(input("Date of Birth: "))
    minutes = get_minutes(dob)
    print(format_minutes(minutes))


def get_date(prompt):
    try:
        return date.fromisoformat(prompt)
    except ValueError:
        print("Invalid date")
        sys.exit()


def get_minutes(date_of_birth):
    days = str(operator.sub(date.today(), date_of_birth))
    match = re.search(r"^(\d+) days, 0:00:00$", days)
    minutes = int(match.group(1)) * 24 * 60
    return minutes


def format_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()




# import inflect
# import operator
# import re
# import sys
# from datetime import date
#
#
# class Seasons:
#     @classmethod
#     def get_input(cls):
#         try:
#             date_of_birth = date.fromisoformat(input("Date of Birth: "))
#         except ValueError:
#             sys.exit()
#         return cls(date_of_birth)
#
#     def __init__(self, date_of_birth):
#         self.date_of_birth = date_of_birth
#
#     @property
#     def date_of_birth(self):
#         return self._date_of_birth
#
#     @date_of_birth.setter
#     def date_of_birth(self, date_of_birth):
#         self._date_of_birth = date_of_birth
#
#     def __str__(self):
#         p = inflect.engine()
#         diff_in_days = str(operator.sub(date.today(), self.date_of_birth))
#         days = re.search(r"^(\d+) days, 0:00:00$", diff_in_days)
#         minutes = int(days.group(1)) * 24 * 60
#         word = p.number_to_words(minutes, andword="")
#         return f"{word.capitalize()} minutes"
#
#
# def main():
#     season_1 = Seasons.get_input()
#
#     print(season_1)
#
#
# if __name__ == "__main__":
#     main()


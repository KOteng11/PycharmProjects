def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Ask user to enter date and call the get_date function
    month, day, year = get_date("Date: ", months)
    # print date in YYYY-MM-DD format
    print(f"{year}-{month:02}-{day:02}")


def get_date(prompt, list_of_months):
    """

    :param prompt:
    :param list_of_months:
    :return: month, day, year
    """
    while True:
        try:
            # Display prompt
            user_date = input(prompt)
            # split date into months, days and years
            if "/" in user_date:
                mm, dd, yyyy = user_date.split("/")
                if 1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
                    return int(mm), int(dd), int(yyyy)
            else:
                mm, dd, yyyy = user_date.split()
                dd = str(dd)
                if "," in dd:
                    dd = dd.replace(",", "")
                else:
                    continue
                if mm in list_of_months and 1 <= int(dd) <= 31:
                    mm = list_of_months.index(mm) + 1
                    return int(mm), int(dd), int(yyyy)
        except ValueError:
            pass


main()


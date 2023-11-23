def check_leap_year(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Which year do you want to check?: "))

result = check_leap_year(year)

if result:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

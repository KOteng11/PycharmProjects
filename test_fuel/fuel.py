def main():
    str_fraction = input("Fraction: ")
    fuel = convert(str_fraction)
    check_fuel = gauge(fuel)
    print(check_fuel)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)

        if numerator > denominator > 0:
            raise ValueError
        return round((numerator / denominator) * 100)
    except ZeroDivisionError:
        raise
    except ValueError:
        raise



if __name__ == "__main__":
    main()

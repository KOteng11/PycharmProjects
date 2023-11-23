def main():
    # Ask user for time
    get_time = input("What time is it? ").strip()

    # Convert time into decimal
    formatted_time = convert(get_time)

    print(formatted_time)
    print(type(formatted_time))
    # Display meal type based on time
    print(display_meal(formatted_time))


def convert(time):
    """
    This function convert time into float and returns it in 2 decimal place
    :param time:
    :return: time
    """
    hours, minutes = time.split(":")
    if minutes.endswith("am"):
        minutes = minutes.replace("am", "").strip()
    elif minutes.endswith("pm"):
        minutes = minutes.replace("pm", "").strip()
        hours = float(hours) + 12
    minutes = float(minutes) / 600 * 10
    return float(hours) + minutes


def display_meal(time):
    if 7.0 <= time <= 8.0:
        return "breakfast time"
    elif 12.0 <= time <= 13.0:
        return "lunch time"
    elif 18.0 <= time <= 19.0:
        return "dinner time"


if __name__ == "__main__":
    main()


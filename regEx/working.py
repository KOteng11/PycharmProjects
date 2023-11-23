import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^((?:[1-9]|1[0-2]):?[0-5]?\d?\s(?:AM|PM)) to ((?:[1-9]|1[0-2]):?[0-5]?\d?\s(?:AM|PM))$",
                            s):
        time_1 = split_time(matches.group(1))
        time_1[0] = int(time_1[0])
        time_2 = split_time(matches.group(2))
        time_2[0] = int(time_2[0])

        if matches.group(1).endswith("PM") and time_1[0] < 12:
            time_1[0] += 12

        if matches.group(2).endswith("PM") and time_2[0] < 12:
            time_2[0] += 12

        return format_time(time_1, time_2)

    else:
        raise ValueError(sys.exit("Incorrect Time Format"))


def format_time(t_1, t_2):
    if t_1[0] < 10:
        t_1[0] = f"{t_1[0]:02}"
    if t_2[0] < 10:
        t_2[0] = f"{t_2[0]:02}"
    if t_1[1].isdigit() and t_2[1].isdigit():
        return f"{t_1[0]}:{t_1[1]} to {t_2[0]}:{t_2[1]}"
    else:
        return f"{t_1[0]}:00 to {t_2[0]}:00"


def split_time(time):
    if ":" in time:
        t1 = re.split(" ", time)
        return re.split(":", t1[0])
    else:
        return re.split(" ", time)


if __name__ == "__main__":
    main()

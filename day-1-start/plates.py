def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 2:
        return s[:2].isalpha()
    if 2 < len(s) <= 6:
        if s[2:].isalpha():
            return True
        elif s[2:].isdigit() and s[2] != "0":
            return True
        elif s[2:].isalnum():
            for i in range(2, len(s)):
                if s[i].isdigit() and int(s[i]) < 1:
                    return False
                if s[i].isdigit() and s[-1].isalpha():
                    print(s[i])
                    return False
                elif s[i].isdigit() and int(s[i]) == 0:
                    return False

                # elif s[i] == "0":
        else:
            return False
    else:
        return False


main()
def main():
    student_heights = input("Input a list of student  heights: ").split()

    print(get_average(student_heights))


def get_average(heights):
    total = 0
    count = 0
    for height in heights:
        total += int(height)
        count += 1
    return round(total/count)


main()

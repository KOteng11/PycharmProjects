def main():
    print(f"The sum of all even number between 1 and 100 is: {sum_even()}")


def sum_even():
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    return total


main()

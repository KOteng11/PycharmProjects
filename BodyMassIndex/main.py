def main():
    height: float = get_height("Enter Height: ")
    weight: int = get_weight("Enter Weight: ")

    bmi: str = calculate_bmi(height, weight)

    print(f"{bmi}")


def calculate_bmi(height: float, weight: float) -> str:
    return f"{weight / height ** 2:.2f}"


def get_height(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass


def get_weight(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == "__main__":
    main()

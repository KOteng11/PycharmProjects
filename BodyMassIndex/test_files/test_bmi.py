from main import calculate_bmi


def test_calculate_bmi() -> None:
    assert calculate_bmi(1.65, 72) == "26.45"

from final_project_rewrite import split_bill, calculate_total_bill, get_tip


def test_split_bill_with_tip() -> None:
    assert split_bill(187.0, 4) == 46.75
    assert split_bill(150.0, 5) == 30.0


def test_calculate_total_bill() -> None:
    assert calculate_total_bill(170, 10.4) == 180.4
    assert calculate_total_bill(170, 0) == 170.0


def test_get_tip() -> None:
    assert get_tip(170, 10) == 17.0
    assert get_tip(170, 12) == 20.4

from project import *


def test_split_bill():
    assert split_bill(89, 3) == 29.67
    assert split_bill(57.90, 5) == 11.58


def test_calculate_total_bill():
    assert calculate_total_bill(30, 3) == 33.00
    assert calculate_total_bill(100, 10) == 110


def test_calculate_tip():
    assert calculate_tip(100, 10) == 10.0
    assert calculate_tip(450, 12) == 54.0

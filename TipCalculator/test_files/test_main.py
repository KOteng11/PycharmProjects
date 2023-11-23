from main import *


def test_get_tip():
    """ tip used is 10 percent which results $17 tip"""
    assert get_tip("Enter tip: ", 170) == 17
    """ tip used is 12 percent which results in $20.4 tip"""
    assert get_tip("Enter tip: ", 170) == 20.4


def test_get_total_bill() -> None:
    """ adds 17 to 170 which results in 187"""
    assert get_total_bill(170, 17) == 187
    """ adds 20.4 to 170 which results in 190.4"""
    assert get_total_bill(170, 20.4) == 190.4

def test_split_bill() -> None:
    assert split_bill(187, 5) == 37.4
    assert split_bill(190.4, 5) == 38.08


import pytest
from add import *


def test_divide_by_zero() -> None:
    """dividing by zero should exit the system"""
    with pytest.raises(SystemExit):
        divide(3, 0)


def test_divide() -> None:
    """dividing 2 by 2 should be 1"""
    assert divide(2, 2) == 1


def test_add() -> None:
    """ sum of 4 and 3 should be 7"""
    assert add(4, 3) == 7


def test_multiply() -> None:
    """multiplying 4 and 3 should be 12"""
    assert multiply(4, 3) == 12


def test_subtract() -> None:
    """ difference of 4 and 3 should be 1"""
    assert subtract(4, 3) == 1











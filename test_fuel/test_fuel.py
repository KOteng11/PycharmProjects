from fuel import convert, gauge
import pytest


def test_fraction():
    assert convert("1/100") == 1
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    with pytest.raises(ValueError):
        convert("cat/2")


def test_compare():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

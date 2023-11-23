from calculator import square
import pytest


def test_positive() -> None:
    assert square(2) == 4
    assert square(3) == 9


def test_negative() -> None:
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero() -> None:
    assert square(0) == 0


def test_str() -> None:
    with pytest.raises(TypeError):
        square("cat")


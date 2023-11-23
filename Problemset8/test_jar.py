from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(5) == "5 cookies has been added successfully"
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)
    assert jar.deposit(5) == "5 cookies has been added successfully"
    assert jar.withdraw(2) == "2 cookies has been removed successfully"





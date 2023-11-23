from bank import value


def test_hello():
    assert value("hello, Kingsley") == "$0"


def test_h():
    assert value("howdy, Kingsley") == "$20"


def test_everything_else():
    assert value("Bonjour, Kingsley") == "$100"

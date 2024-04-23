from bank import value


def test_value_start_with_h():
    assert value("Hover board!") == 20
    assert value("Hit me pls in the face") == 20
    assert value("hey, Hello, mister") == 20


def test_value_start_with_hello():
    assert value("Hello moto") == 0
    assert value("hello mr robot") == 0


def test_value_starts_with_other():
    assert value("Glad to see you!") == 100
    assert value("Please welcome sir") == 100

from jar import Jar
import pytest


def test_jar():
    assert Jar(13)


def test_init():
    with pytest.raises(ValueError):
        Jar()
    with pytest.raises(ValueError):
        Jar(0)
    with pytest.raises(ValueError):
        Jar("10")


def test_capacity():
    jar = Jar(20)
    assert jar.capacity == 20


def test_deposite_exceed():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposite(6)


def test_size():
    jar = Jar(11)
    assert jar.size == 0
    jar.deposite(7)
    assert jar.size == 7
    jar.withdraw(2)
    assert jar.size == 5


def test_withdraw_too_many():
    jar = Jar(5)
    jar.deposite(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)


def test_str():
    jar = Jar(5)
    jar.deposite(2)
    assert str(jar) == "🍪🍪"
    jar.deposite(1)
    assert str(jar) == "🍪🍪🍪"

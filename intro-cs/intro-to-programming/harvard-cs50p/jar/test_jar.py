from jar import Jar
import pytest


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    jar = Jar()
    assert jar.capacity == 12


def test_init_fail():
    with pytest.raises(ValueError):
        Jar(0)
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("10")


def test_capacity():
    jar = Jar(20)
    assert jar.capacity == 20


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(3)
    assert jar.size == 3


def test_size():
    jar = Jar(11)
    assert jar.size == 0
    jar.deposit(7)
    assert jar.size == 7
    jar.withdraw(2)
    assert jar.size == 5


def test_withdraw():
    jar = Jar(10)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar.deposit(6)
    jar.withdraw(8)
    assert jar.size == 0


def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"

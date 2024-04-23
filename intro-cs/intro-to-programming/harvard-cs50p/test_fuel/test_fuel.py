from fuel import convert, gauge
import pytest


def test_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("4")
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

from seasons import minutes_from_date
from datetime import date, timedelta
import pytest


def test_calc_minutes_365_days():
    _date = date.today() - timedelta(days=365)
    assert(
        minutes_from_date(str(_date))
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_calc_minutes_13_days():
    _date = date.today() - timedelta(days=13)
    assert(
        minutes_from_date(str(_date))
        == "Eighteen thousand, seven hundred twenty minutes"
    )


def test_calc_minutes_invalid_date():
    with pytest.raises(SystemExit):
        minutes_from_date("")
    with pytest.raises(SystemExit):
        minutes_from_date("January 1, 1999")
    with pytest.raises(SystemExit):
        minutes_from_date("foobar")

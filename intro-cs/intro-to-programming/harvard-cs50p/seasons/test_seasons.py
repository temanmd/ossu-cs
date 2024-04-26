from seasons import calc_minutes, format_to_words
from datetime import date, timedelta
import pytest


def test_format_to_words_365_days():
    minutes = 365 * 24 * 60
    assert(
        format_to_words(minutes)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_format_to_words_13_days():
    minutes = 13 * 24 * 60
    assert(
        format_to_words(minutes)
        == "Eighteen thousand, seven hundred twenty minutes"
    )


def test_calc_minutes():
    _date = date.today() - timedelta(days=365)
    assert calc_minutes(str(_date)) == 525_600
    _date = date.today() - timedelta(days=3)
    assert calc_minutes(str(_date)) == 4320


def test_calc_minutes_invalid_date():
    with pytest.raises(SystemExit):
        calc_minutes("")
    with pytest.raises(SystemExit):
        calc_minutes("January 1, 1999")
    with pytest.raises(SystemExit):
        calc_minutes("foobar")

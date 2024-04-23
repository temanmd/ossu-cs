from numb3rs import validate


def test_validate_true():
    assert validate("123.25.0.12") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("140.20.235.144") == True
    assert validate("123.01.0.12") == True
    assert validate("123.00.0.12") == True
    assert validate("123.021.0.12") == True


def test_validate_false():
    assert validate("123.267.0.12") == False
    assert validate("1.0.0.0.0") == False
    assert validate("foobar") == False
    assert validate("ip.ad.dr.ess") == False

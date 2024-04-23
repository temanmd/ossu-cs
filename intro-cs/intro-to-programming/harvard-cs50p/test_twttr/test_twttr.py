from twttr import shorten


def test_shorten():
    assert shorten("Computer Sience") == "Cmptr Snc"
    assert shorten("hEllo, wOrld!") == "hll, wrld!"
    assert shorten("  __kJg 00 +aA") == "  __kJg 00 +"

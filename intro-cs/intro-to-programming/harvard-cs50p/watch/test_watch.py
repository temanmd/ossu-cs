from watch import parse


def test_watch():
    html = "<iframe src=\"http://www.youtube.com/embed/xvFZjo5PgG0\"></iframe>"
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

    html = "<iframe src=\"https://www.youtube.com/embed/xvFZjo5PgG0\"></iframe>"
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

    html = "<iframe src=\"https://youtube.com/embed/xvFZjo5PgG0\"></iframe>"
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

    html = "<iframe src=\"https://google.com\"></iframe>"
    assert parse(html) == None

import pytest
from lines import get_file, lines


def test_get_file_empty_args():
    with pytest.raises(SystemExit) as sys_exit:
        get_file([])
    assert sys_exit.value.code == "Too few command-line arguments"


def test_get_file_too_many_args():
    with pytest.raises(SystemExit) as sys_exit:
        get_file(["names.py", "hello.py"])
    assert sys_exit.value.code == "Too many command-line arguments"


def test_get_file_wrong_file():
    with pytest.raises(SystemExit) as sys_exit:
        get_file(["names.txt"])
    assert sys_exit.value.code == "Not a Python file"


def test_get_file_does_not_exist():
    with pytest.raises(SystemExit) as sys_exit:
        get_file(["some_secret.py"])
    assert sys_exit.value.code == "File does not exist"


def test_lines():
    file = get_file(["names.py"])
    assert lines(file) == 4


def test_lines_with_comments():
    file = get_file(["names_comments.py"])
    assert lines(file) == 4


def test_lines_with_empty_lines():
    file = get_file(["names_empty_lines.py"])
    assert lines(file) == 4


def test_lines_with_space_lines():
    file = get_file(["names_space_lines.py"])
    assert lines(file) == 4

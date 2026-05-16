from ci_python_lab.calculator import add, is_even, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_is_even():
    assert is_even(10) is True
    assert is_even(7) is False

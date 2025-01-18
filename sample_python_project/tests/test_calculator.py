import pytest
from calculator.calculator import add, sub, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(2,1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
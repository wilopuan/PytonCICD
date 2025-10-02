import pytest
from mypkg.math_ops import add, multiply, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(2.5, 0.5) == 3.0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2.5, 2) == 5.0


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.5)

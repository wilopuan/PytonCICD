import pytest
from mypkg.utils import greet, is_even


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    with pytest.raises(TypeError):
        is_even(2.5)

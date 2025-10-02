"""Basic math operations used for examples and tests."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b


def factorial(n: int) -> int:
    """Compute factorial iteratively.

    Raises ValueError for negative inputs and TypeError for non-integers.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

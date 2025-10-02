"""Utility helpers for the example package."""

def greet(name: str) -> str:
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"


def is_even(n: int) -> bool:
    """Return True if n is even; raises TypeError for non-integers."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return (n % 2) == 0

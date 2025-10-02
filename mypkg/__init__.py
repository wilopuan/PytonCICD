"""mypkg package - small example package with basic modules
"""
from .math_ops import add, multiply, factorial
from .utils import greet, is_even

__all__ = ["add", "multiply", "factorial", "greet", "is_even"]

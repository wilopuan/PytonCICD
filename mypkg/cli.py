"""Small CLI entrypoint demonstrating package usage."""

import argparse
from .math_ops import add


def main(argv=None):
    parser = argparse.ArgumentParser(prog="mypkg")
    parser.add_argument("a", type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")
    args = parser.parse_args(argv)
    result = add(args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()

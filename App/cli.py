"""Simple CLI for the App package."""
import argparse

from .config import APP_NAME, DEFAULT_GREETING


def build_parser():
    p = argparse.ArgumentParser(prog=APP_NAME, description="Simple demo app CLI")
    p.add_argument("--name", "-n", default=None, help="Name to greet")
    p.add_argument("--version", "-v", action="store_true", help="Show package version")
    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        # avoid importing pkg_resources; use package attribute if available
        try:
            from . import __version__ as version
        except Exception:
            version = "unknown"
        print(f"{APP_NAME} version {version}")
        return 0

    name = args.name or DEFAULT_GREETING
    print(f"Hello, {name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

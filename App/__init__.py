"""Small application package initializer for App.

Provides a minimal public API: version and run().
"""
from .cli import main as run
from .config import APP_NAME

__all__ = ["run", "APP_NAME"]

__version__ = "0.1.0"

# mypkg — minimal Python project example

This repository contains a tiny Python package named `mypkg` that demonstrates a few modules, a CLI, and tests.

Quick start

1. Create a virtual environment (optional but recommended):

   Windows PowerShell

   ```powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
   ```

2. Install the test dependency:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Run the test suite:

   ```powershell
   python -m pytest -q
   ```

Package contents

- `mypkg/math_ops.py` — add, multiply, factorial
- `mypkg/utils.py` — small helpers
- `mypkg/cli.py` — example CLI using `argparse`
- `tests/` — pytest tests

Feel free to extend the package with more modules and CI later.

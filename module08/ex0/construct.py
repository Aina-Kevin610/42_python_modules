#!/usr/bin/env python3

import os
import site
import sys


if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in")

    print()

    print("Current python: ", sys.prefix)
    print("Virtual Environment: None detected")

    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print()

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

    print()

    print("Then run this program again.")
else:
    print("MATRIX STATUS: Welcome to the construct")

    print()

    print("Current python: ", sys.prefix)
    print("Virtual Environment: None detected")

    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
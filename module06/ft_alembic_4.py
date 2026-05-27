#!/usr/bin/env python3

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", alchemy.create_air())
    print("\nNow show that not all functions can be reached")
    print("this will raise an exception\n")
    try:
        print(alchemy.create_earth())
    except AttributeError as e:
        print("Error - ", e)

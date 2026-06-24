#!/usr/bin/env python3

import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    op = ["add", "multiply", "max", "min",]
    try:
        if operation not in op:
            raise TypeError("unknown operation")
    except TypeError as e:
        print("Error - ", e)
    if operation == "add":
        return functools.reduce(operator.add( ), spells)


if __name__ == "__main__":
    print(spell_reducer([1, 2, 3, 4, 5], "add"))
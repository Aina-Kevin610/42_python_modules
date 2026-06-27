#!/usr/bin/env python3

import functools
import operator
from typing import Any
from collections.abc import Callable

def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def base(param: Any) -> str:
        raise NotImplementedError("Unknown spell type")
    
    @base.register
    def _(param: int) -> str:
        return f"Damage spell: {param} damage"

    @base.register
    def _(param: list) -> str:
        return f"Multi-cast: {len(param)} spells"

    @base.register
    def _(param: str) -> str:
        return f"Enchantment: {param}"

    return base



if __name__ == "__main__":

    print("\nTesting spell dispatcher...")

    disp = spell_dispatcher()

    try:
        print(disp(42))
        print(disp("fireball"))
        print(disp(["boom", "rage", "heal"]))
        print(disp(12.4))
    except Exception as e:
        print(e)
    
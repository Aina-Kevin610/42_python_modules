#!/usr/bin/env python3

import functools

from typing import Any
from collections.abc import Callable



def mage_counter() -> Callable:
    a = 0
    def count() -> int:
        nonlocal a
        a += 1
        return a
    return count


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power
    def act(add: int) -> int:
        nonlocal total
        total += add
        return total
    return act


def enchantment_factory(enchantment_type: str) -> Callable:
    def act(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return act


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, value) -> None:
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def base(param: Any) -> str:
        raise NotImplementedError("Unknown spell type ", param)

    @base.register
    def _(param: int) -> str:
        return f"Damage spell: {param} damage"

    @base.register
    def _(param: list[Any]) -> str:
        return f"Multi-cast: {len(param)} spells"

    @base.register
    def _(param: str) -> str:
        return f"Enchantment: {param}"

    return base


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_1 = mage_counter()
    counter_2 = mage_counter()
    print("Counter_a call 1: ", counter_1(), "...")
    print("Counter_a call 2: ", counter_1(), "...")
    print("Counter_b call 1: ", counter_2(), "...")

    print("\nTesting spell accumulator...")
    act = spell_accumulator(100)
    print("Base 100, add 20: ", act(20))
    print("Base 100, add 30: ", act(30))

    print("\nTesting enchantment factory...")
    enchantment_1 = enchantment_factory("Flaming")
    print(enchantment_1("Sword"))

    enchantment_1 = enchantment_factory("Frozen")
    print(enchantment_1("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault['recall']('secret'))
    print("Recall 'unknown':", vault['recall']('unknown'))


    print("\nTesting spell dispatcher...")

    disp = spell_dispatcher()

    try:
        print(disp(42))
        print(disp("fireball"))
        print(disp(["boom", "rage", "heal"]))
        print(disp(12.4))
    except Exception as e:
        print(e)

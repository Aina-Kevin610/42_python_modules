#!/usr/bin/env python3

from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return (f"Healing potions brewed with '{create_earth()}'"
            f" and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strength potions brewed with '{create_fire()}'"
            f" and '{create_water()}'")


if __name__ == "__main__":
    print(healing_potion())
    print()
    print(strength_potion())

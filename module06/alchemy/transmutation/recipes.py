#!/usr/bin/env python3

from ..elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting "
        f"Lead to Gold: "
        f"brew '[{create_air()}]' "
        f"and '[{strength_potion()}]' "
        f"mixed with '[{create_fire()}]' "
    )

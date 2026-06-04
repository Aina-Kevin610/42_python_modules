#!/usr/bin/env python3

from ex0 import FlameFactory, WaterFactory
from ex1 import HealingCreatureFactory,TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle() -> None:
    pass


if __name__ == "__main__":
    flameling = FlameFactory.create_base(self=None)
    aquabub = WaterFactory.create_base(self=None)
    sproutling = HealingCreatureFactory.create_base(self=None)
    shiftling = TransformCreatureFactory.create_base(self=None)

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defense = DefensiveStrategy()

    print(flameling.describe())
    print(aquabub.describe())
    print(sproutling.describe())
    print(shiftling.describe())

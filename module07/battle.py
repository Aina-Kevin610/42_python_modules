#!/usr/bin/env python3

from ex0.factory import CreatureFactory, FlameFactory, WaterFactory


def deploye(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight(creature_1: CreatureFactory, creature_2: CreatureFactory) -> None:
    print()
    flame = creature_1.create_base()
    water = creature_2.create_base()
    print(flame.describe())
    print(" vs.")
    print(water.describe())
    print(" fight!")
    print(flame.attack())
    print(water.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    water = WaterFactory()
    print("Testing factory")
    deploye(flame)
    print("\nTesting factory")
    deploye(water)
    fight(flame, water)

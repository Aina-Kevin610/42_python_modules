#!/usr/bin/env python3


from ex1 import HealingCreatureFactory


if __name__ == "__main__":
    healing = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    sproutling = healing.create_base()
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print(" evolved:")
    bloomelle = healing.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

#!/usr/bin/env python3


from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory

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

    transform = TransformCreatureFactory()
    print("\nTesting Creature with transform capability")
    shiftling = transform.create_base()
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())

    shiftling.transforming = True
    print(shiftling.attack())
    print(shiftling.revert())

    print(" evolved:")
    morphagon = transform.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    morphagon.transforming = True
    print(morphagon.attack())
    print(morphagon.revert())

    #le polycope jose
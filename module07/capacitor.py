#!/usr/bin/env python3


from ex1.capabilities import Sproutling


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    sproutling = Sproutling()
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print(" evolved:")
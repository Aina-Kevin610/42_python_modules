#!/usr/bin/env python3

from creature import Creature


class Flameling(Creature):
    def __init__(self, name: str, types: str) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Ember!"


class Pyrodon(Creature):
    def __init__(self, name, types) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name, types) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Water Gun!"


class Torragon(Creature):
    def __init__(self, name, types) -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


if __name__ == "__main__":
    f = Flameling("Flameling", "fire")
    p = Pyrodon("Pyrodon", "Fire/Flying")
    a = Aquabub("Aquabub", "Water")
    t = Torragon("Torragon", "Water")

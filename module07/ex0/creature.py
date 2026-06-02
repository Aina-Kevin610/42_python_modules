#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, types: str) -> None:
        self.name = name
        self.type = types

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str = "Flameling", types: str = "Fire") -> None:

        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Ember!"


class Pyrodon(Creature):
    def __init__(
            self,
            name: str = "Pyrodon",
            types: str = "Flying/Fire"
    ) -> None:

        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub", types: str = "Water") -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} use Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon", types: str = "Water") -> None:
        super().__init__(name, types)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


if __name__ == "__main__":
    f = Flameling()
    p = Pyrodon()
    a = Aquabub()
    t = Torragon()

#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transforming: bool = False

    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(
            self,
            name: str = "Sproutling",
            types: str = "Grass"
    ) -> None:

        Creature.__init__(self, name, types)

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount!"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(
            self,
            name: str = "Bloomelle",
            types: str = "Grass/Fairy"
    ) -> None:

        Creature.__init__(self, name, types)

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance !"


class Shiftling(Creature, TransformCapability):
    def __init__(
            self,
            name: str = "Shiftling",
            types: str = "Normal"
    ) -> None:

        Creature.__init__(self, name, types)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        return f"{self.name} shifts into a sharper form!"

    def attack(self) -> str:
        if self.transforming:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attack normally."
    
    def revert(self) -> str:
        return f"{self.name} return to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(
            self,
            name: str = "Morphagon",
            types: str = "Normal/Dragon"
    ) -> None:

        Creature.__init__(self, name, types)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        return f"{self.name} morphs into a dragonic battle form!"

    def attack(self) -> str:
        if self.transforming:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attack normally."
    
    def revert(self) -> str:
        return f"{self.name} stabilizes its form."
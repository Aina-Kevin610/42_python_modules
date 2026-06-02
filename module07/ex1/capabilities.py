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
b.describe
    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance !"


class
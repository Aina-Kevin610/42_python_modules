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
    def __init__(self, name: str, types: str) -> None:
        super.__init__(name, types)

    def heal(self) -> str:
        return f"{self.name} is healing himself!"

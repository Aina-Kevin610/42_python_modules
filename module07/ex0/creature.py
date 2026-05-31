#!/usr/bin/env python3


from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, types: str) -> None:
        self.name = name
        self.type = types

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

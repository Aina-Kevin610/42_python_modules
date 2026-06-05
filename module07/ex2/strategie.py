#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class Invalid(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        try:
            if not self.is_valid(creature):
                raise Invalid("Invalid combinaison!")
            print(creature.attack())
        except Invalid:
            raise ValueError(f"Invalid Creature '{creature.name}' for this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        try:
            if not self.is_valid(creature):
                raise Invalid("Invalid combinaison!")
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        except Invalid:
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        try:
            if not self.is_valid(creature):
                raise Invalid("Invalid combinaison!")
            print(creature.attack())
            print(creature.heal())
        except Invalid:
            raise ValueError(f"Invalid Creature '{creature.name}' for this defensive strategy")

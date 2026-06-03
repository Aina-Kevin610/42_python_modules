#!/usr/bin/env python3

from abs import ABS, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABS):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self) -> str:
        return "this is act"


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability):


    def act(self) -> str:
        return "this is act"
    

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self) -> str:
        return f"hello"
#!/usr/bin/env python3

from ex0.factory import CreatureFactory
from ex1.capabilities import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()
    
    def create_evolved(self) -> Morphagon:
        return Morphagon()

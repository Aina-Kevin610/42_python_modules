#!/usr/bin/env python3

from ex0.factory import CreatureFactory
from .capabilities import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
b.describe
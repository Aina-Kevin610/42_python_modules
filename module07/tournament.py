#!/usr/bin/env python3

from ex0 import FlameFactory, WaterFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from typing import Any


def battle(opponents: list[tuple[Any, Any]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i, opponent in enumerate(opponents):
        for creature in opponents[i + 1:]:
            try:
                print("\n* Battle *")
                print(opponent[0].describe())
                print(" vs")
                print(creature[0].describe())
                print(" now fight!")
                opponent[1].act(opponent[0])
                creature[1].act(creature[0])
            except Exception as e:
                print("Battle error, aborting tournament: ", e)


if __name__ == "__main__":
    flameling = FlameFactory().create_base()
    aquabub = WaterFactory().create_base()
    sproutling = HealingCreatureFactory().create_base()
    shiftling = TransformCreatureFactory().create_base()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defense = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flameling, normal), (sproutling, defense)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flameling, aggressive), (sproutling, defense)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aquabub, normal), (sproutling, defense), (shiftling, aggressive)])

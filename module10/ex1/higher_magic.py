#!/usr/bin/env python3

from collections.abc import Callable
import random


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def rage(target: str, power: int) -> str:
    return f"Rage raise {target}'s power to {power}"


def condition(power: int) -> bool:
    return power >= 10


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[], tuple[str, str]]:
    values = [8, 12, 22]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def result() -> tuple[str, str]:
        return (
            spell1(random.choice(targets), random.choice(values)),
            spell2(random.choice(targets), random.choice(values)),
        )

    return result


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    def result(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return result


def conditional_caster(
    condition: Callable[[int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def result(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return result


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[], list[str]]:
    def result() -> list[str]:
        res = []
        values = [8, 12, 22]
        targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
        for spell in spells:
            choice_target = random.choice(targets)
            choice_value = random.choice(values)
            res.append(spell(choice_target, choice_value))
        return res

    return result


if __name__ == "__main__":

    combined = spell_combiner(heal, rage)
    print(combined())

    mega_rage = power_amplifier(rage, 5)
    print(mega_rage('Knight', 10))

    conditional = conditional_caster(condition, rage)
    print(conditional('Dragon', 12))

    listed = spell_sequence([rage, heal])
    print(listed())

#/usr/bin/env python3

from collections.abc import Callable
import random


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def rage(target: str, power: int) -> str:
    return f"Rage raise {target}'s power to {power}"


def condition(power: int) -> bool: 
    return power >= 10


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    values = [8, 12, 22]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    def result() -> tuple[str, str]:
        return (
            spell1(random.choice(targets), random.choice(values)),
            spell2(random.choice(targets), random.choice(values))
            )
    return result


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def result(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return result


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def result(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return result


def spell_sequence(spells: list[Callable]) -> Callable:
    def result() -> list[str]:
        res = []
        values = [8, 12, 22]
        targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
        for spell in spells:
            res.append(spell(random.choice(targets), random.choice(values)))
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

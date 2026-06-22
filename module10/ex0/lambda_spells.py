#!/usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, int]]:
    return sorted(artifacts, key=lambda x: x["power"])


def power_filter(mages: list[dict[str, Any]],
                 min_power: int
                 ) -> list[dict[str, int]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: ("* " + x + " *"), spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    min_power = min(mages, key=lambda x: x["power"])
    max_power = max(mages, key=lambda x: x["power"])
    average = round(sum([x["power"] for x in mages]) / len(mages), 2)

    return {"max_power": max_power["power"],
            "min_power": min_power["power"],
            "avg_power": average
            }


if __name__ == "__main__":
    artifacts = [{'name': 'Lightning Rod', 'power': 80, 'type': 'relic'},
                 {'name': 'Shadow Blade', 'power': 73, 'type': 'weapon'},
                 {'name': 'Crystal Orb', 'power': 84, 'type': 'accessory'},
                 {'name': 'Ice Wand', 'power': 62, 'type': 'focus'}
                 ]
    
    mages = [{'name': 'Sage', 'power': 62, 'element': 'light'},
             {'name': 'River', 'power': 56, 'element': 'shadow'},
             {'name': 'Nova', 'power': 82, 'element': 'water'},
             {'name': 'Morgan', 'power': 51, 'element': 'wind'},
             {'name': 'Rowan', 'power': 80, 'element': 'shadow'}
             ]
    
    spells = ['heal', 'flash', 'darkness', 'freeze']

    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting power filter...")
    print(power_filter(mages, 60))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage_stats...")
    print(mage_stats(mages))

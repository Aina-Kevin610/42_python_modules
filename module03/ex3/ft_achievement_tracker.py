#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#    ft_achievement_tracker.py                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: airandri <airandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 07:21:18 by airandri            #+#    #+#            #
#   Updated: 2026/04/20 07:21:23 by airandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


all_achievements: list = [
    'Crafting Genius',
    'Strategist',
    'World Savior',
    'Speed Runner',
    'Survivor',
    'Master Explorer',
    'Treasure Hunter',
    'Unstoppable',
    'First Steps',
    'Collector Supreme',
    'Sharp Mind',
    'Boss Slayer',
    'Untouchable',
    'Hidden Path Finder'
]


class Player:
    def __init__(self, name: str, achievement: set) -> None:
        self.name = name
        self.achievement = achievement


def gen_player_achievements() -> set:
    nb = random.randint(1, 14)
    achievement = random.sample(all_achievements, nb)
    return (set(achievement))


def main() -> None:
    alice = Player("Alice", gen_player_achievements())
    bob = Player("Bob", gen_player_achievements())
    charlie = Player("Charlie", gen_player_achievements())
    dylan = Player("Dylan", gen_player_achievements())

    print("Player Alice: ", alice.achievement)
    print("Player Bob: ", bob.achievement)
    print("Player Charlie: ", charlie.achievement)
    print("Player Dylan: ", dylan.achievement)
    print("\nAll distinct achievements: ", set(all_achievements))
    common = alice.achievement.intersection(bob.achievement,
                                            charlie.achievement,
                                            dylan.achievement)
    print("\nCommon achievements: ", common)
    only = alice.achievement.difference(bob.achievement,
                                        charlie.achievement,
                                        dylan.achievement)
    print("\nOnly Alice has:", only)
    only = bob.achievement.difference(alice.achievement,
                                      charlie.achievement,
                                      dylan.achievement)
    print("Only Bob has:", only)
    only = charlie.achievement.difference(bob.achievement,
                                          alice.achievement,
                                          dylan.achievement)
    print("Only Charlie has:", only)
    only = dylan.achievement.difference(bob.achievement,
                                        charlie.achievement,
                                        alice.achievement)
    print("Only Dylan has:", only)
    missing = set(all_achievements).difference(alice.achievement)
    print("\nAlice is missing: ", missing)
    missing = set(all_achievements).difference(bob.achievement)
    print("Bob is missing: ", missing)
    missing = set(all_achievements).difference(charlie.achievement)
    print("Charlie is missing: ", missing)
    missing = set(all_achievements).difference(dylan.achievement)
    print("Dylan is missing: ", missing)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()

#!/usr/bin/env python3

import random


def main():
    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin',
               'Liam']
    players_cap = [player.capitalize() for player in players]
    only_player_capt = [player
                        for
                        player in players
                        if player == player.capitalize()]
    print("Initial list of players: ", players)
    print("New list with all name capitalized: ", players_cap)
    print("New list of capitalized names only:", only_player_capt)
    scores = {player: random.randint(0, 1000) for player in players_cap}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    only_score = {key: value
                  for key, value in scores.items()
                  if value > average}
    print("High scores: ", only_score)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    main()

import random


def main():
    players = ['Alice', 'bob', 'Charlie', 'dylan',
            'Emma', 'Gregory', 'john', 'kevin',
            'Liam'
            ]
    players_cap = [player.capitalize() for player in players]
    only_player_capt = [player for player in players if player == player.capitalize()]
    print(f"Initial list of players: ", players)
    print(f"New list with all name capitalized: ", players_cap)
    print(f"New list of capitalized names only:", only_player_capt)
    scores = {player:random.randint(0, 1000) for player in players_cap}
    print(f"Score dict: {scores}")
    only_score = {key : max(value) for key, value in scores.items()}
    print(only_score)

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    main()

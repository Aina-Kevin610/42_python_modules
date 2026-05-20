#!/usr/bin/env python3

import sys


class InvalidParams(Exception):
    pass


def raise_error(scores: list, params: int) -> None:
    if params <= 1:
        raise InvalidParams()
    for score in scores:
        score = int(score)


def error_handler(scores: list, params: int) -> list:
    m1: str = "python3 ft_score_analytics.py <score1> <score2> ..."
    m: str = f"No scores provided. Usage: {m1}"
    result = []
    for score in scores:
        try:
            if params <= 1:
                raise InvalidParams()
            score = int(score)
            if score < 0:
                raise ValueError("Invalid value, score must be positif")
            result.append(score)
        except InvalidParams:
            print(m)
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    return (result)


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list = [score for score in sys.argv if score != sys.argv[0]]
    scores = error_handler(scores, len(sys.argv))
    try:
        Average = sum(scores) / len(scores)
        print("Scores processed: ", scores)
        print("Total Player: ", len(scores))
        print("Average score: ", Average)
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range: ", max(scores) - min(scores))
    except ZeroDivisionError:
        print("No scores provided. Usage:", end=" ")
        print("python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Unknown error happened!")


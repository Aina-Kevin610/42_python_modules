#!/usr/bin/env python3

import sys


class InvalidParams(Exception):
    pass


def raise_error(scores: list[int], params: int) -> None:
    if params <= 1:
        raise InvalidParams()
    for score in scores:
        score = int(score)


def error_handler(row_scores: list[str], params: int) -> list[int]:
    m1: str = "python3 ft_score_analytics.py <score1> <score2> ..."
    m: str = f"No scores provided. Usage: {m1}"
    result = []
    for scores in row_scores:
        try:
            if params <= 1:
                raise InvalidParams()
            score = int(scores)
            if score < 0:
                raise ValueError("Invalid value, score must be positif")
            result.append(score)
        except InvalidParams:
            print(m)
        except ValueError:
            print(f"Invalid parameter: '{scores}'")
    return result


def main() -> None:
    print("=== Player Score Analytics ===")
    row_scores: list[str] = [score for score in sys.argv if score != sys.argv[0]]
    scores: list[int] = error_handler(row_scores, len(sys.argv))
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

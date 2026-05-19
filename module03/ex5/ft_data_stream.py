#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
    players = [
            "bob",
            "alice",
            "dylan",
            "charlie"
            ]

    actions = ['run',
               'eat',
               'sleep',
               'grab',
               'move',
               'climb',
               'swim',
               'release',
               'use'
               ]
    yield (random.choice(players), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[list, None, None]:
    while events:
        idx = random.randrange(len(events))
        choice = events[idx]
        print("Got event from list: ", choice)
        del events[idx]
        yield events


def main() -> None:
    for i in range(0, 1000):
        event = next(gen_event())
        print(f"Event {i}: players {event[0]} did action {event[1]}")
    new_event = [next(gen_event()) for _ in range(0, 10)]
    print("Built list of 10 events: ", new_event, "\n")
    for i in range(0, 10):
        print("Remain in list: ", next(consume_event(new_event)), "\n")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()

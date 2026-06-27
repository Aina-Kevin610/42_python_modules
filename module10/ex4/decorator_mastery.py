#!/usr/bin/env python3


import time
from typing import Any
from collections.abc import Callable
import functools


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., Any]],
                                                Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                power = args[-1]
            else:
                return "Insufficient power for this spell"

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]],
                                               Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for tentative in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... (attempt \
                        {tentative}/{max_attempts})"
                    )
                    time.sleep(0.5)
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        no_space = name.replace(" ", "")
        return no_space.isalpha() if no_space else False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        return "Fireball cast!"

    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError()

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def orc_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(orc_spell() + "\n")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("42"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
